from nicegui import ui, app, run
from sidebar import show_sidebar
import requests
from utils.api import base_url
from typing import List, Dict, Any
import csv
import io


@ui.page("/auth/reports")
async def show_reports():
    """Creates the UI for the admin reports management page."""
    # --- Security Check ---
    role = app.storage.user.get("role")
    if role not in ["admin", "authorities"]:
        ui.notify("You are not authorized to view this page.", type="negative")
        ui.navigate.to("/login")
        return

    show_sidebar()

    # Main content area
    with ui.column().classes(
        "w-full h-full p-8 bg-gray-50 overflow-auto flex flex-col"
    ):
        ui.label("Manage Reports").classes("text-4xl font-bold text-gray-800 mb-8")

        # Filter and Search Section
        with ui.row().classes("w-full justify-between items-center mb-6 gap-4"):
            with ui.input(placeholder="Search reports...").props(
                "outlined dense"
            ).classes("w-full sm:w-64") as search_input:
                ui.icon("search").classes("cursor-pointer").add_slot("prepend")
            status_select = (
                ui.select(
                    [
                        "All",
                        "Pending",
                        "In Progress",
                        "Resolved",
                        "Rejected",
                    ],
                    value="All",
                    label="Status",
                )
                .props("outlined dense")
                .classes("w-40")
            )
            export_button = ui.button("Export CSV", icon="download").props(
                "color=black"
            )

        async def fetch_all_reports(
            search_term: str | None = None, status_filter: str | None = None
        ) -> List[Dict[str, Any]] | None:
            """Fetches all reports from the API for admin/authority view."""
            token = app.storage.user.get("access_token")
            headers = {"Authorization": f"Bearer {token}"}
            params = {}

            # Add search and filter parameters if they are provided
            if search_term:
                # Assuming the backend can filter by title
                params["title"] = search_term

            # Map frontend display values to backend expected values for filtering
            if status_filter and status_filter != "All":
                status_map = {
                    "Pending": "pending",
                    "In Progress": "in-progress",
                    "Resolved": "completed",
                    "Rejected": "rejected",
                }
                # Use the mapped value, or default to lowercase if not in map
                params["status"] = status_map.get(status_filter, status_filter.lower())

            def send_request():
                try:
                    return requests.get(
                        f"{base_url}/issues", headers=headers, params=params
                    )
                except requests.exceptions.RequestException as e:
                    return e

            result = await run.io_bound(send_request)

            if isinstance(result, requests.exceptions.RequestException):
                ui.notify(f"Could not connect to the server: {result}", type="negative")
                return None
            elif result.status_code == 200:
                try:
                    json_data = result.json()
                    # Check if the response is a dictionary with a 'data' key
                    if (
                        isinstance(json_data, dict)
                        and "data" in json_data
                        and isinstance(json_data["data"], list)
                    ):
                        return json_data["data"]
                    # Or if it's directly a list (for APIs that might return it directly)
                    elif isinstance(json_data, list):
                        return json_data
                    else:
                        ui.notify(
                            "API returned unexpected data format (not a list of reports).",
                            type="negative",
                        )
                        return None
                except requests.exceptions.JSONDecodeError:
                    ui.notify(
                        "API returned invalid JSON for reports.",
                        type="negative",
                    )
                    return None
            else:
                ui.notify(
                    f"An error occurred while fetching reports: {result.text}",
                    type="negative",
                )
                return None

        # Table of reports
        with ui.card().classes(
            "w-full shadow-lg rounded-xl flex-grow flex flex-col p-4"
        ).props("flat bordered"):
            columns = [
                {
                    "name": "id",
                    "label": "Report ID",
                    "field": "id",
                    "required": True,
                    "align": "left",
                    "sortable": True,
                },
                {
                    "name": "category",
                    "label": "Category",
                    "field": "category",
                    "sortable": True,
                },
                {
                    "name": "location",
                    "label": "Location",
                    "field": "region",
                    "align": "left",
                },
                {"name": "status", "label": "Status", "field": "status"},
            ]

            table = ui.table(columns=columns, rows=[], row_key="id").classes("w-full")

            def export_csv():
                """Exports the current table data to a CSV file."""
                if not table.rows:
                    ui.notify("No data to export.", type="warning")
                    return

                output = io.StringIO()
                # Use the 'field' for keys
                writer = csv.DictWriter(
                    output,
                    fieldnames=[col["field"] for col in columns],
                    extrasaction="ignore",
                )

                # Write header using column labels
                header = {col["field"]: col["label"] for col in columns}
                writer.writerow(header)

                # Write data rows
                writer.writerows(table.rows)

                # Trigger download
                ui.download(output.getvalue().encode(), "reports.csv")

            export_button.on("click", export_csv)

            async def update_table():
                """Fetches new data based on filters and updates the table."""
                spinner.set_visibility(True)
                table.rows = []  # Clear table while loading
                new_rows = await fetch_all_reports(
                    search_term=search_input.value, status_filter=status_select.value
                )
                if new_rows is not None:
                    table.rows = new_rows
                spinner.set_visibility(False)

            spinner = ui.spinner(size="lg").classes("self-center my-8")

            # Use a JS-based slot for the status badge for maximum compatibility.
            # This avoids the issues with the Python slot object in older NiceGUI versions.
            table.add_slot(
                "body-cell-status",
                r"""
                <q-td :props="props">
                    <q-badge
                        :color="({
                            'pending': 'orange',
                            'in-progress': 'blue',
                            'completed': 'green',
                            'rejected': 'red'
                        })[props.row.status] || 'grey'"
                        class="px-2 py-1 text-xs font-medium"
                    >
                        {{ ({'pending': 'Pending', 'in-progress': 'In Progress', 'completed': 'Resolved', 'rejected': 'Rejected'})[props.row.status] || props.row.status }}
                    </q-badge>
                </q-td>
            """,
            )

            # Bind filter inputs to the update function
            search_input.on("keydown.enter", update_table)
            status_select.on("update:model-value", update_table)

            await update_table()  # Initial data load
