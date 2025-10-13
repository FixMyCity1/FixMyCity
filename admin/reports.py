from nicegui import ui, app
from .sidebar import show_sidebar


@ui.page("/admin/reports")
def show_reports():
    """Creates the UI for the admin reports management page."""
    # The sidebar must be a top-level element.
    # The main content will automatically be placed to its right.
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
            with ui.row().classes("gap-4"):
                ui.select(
                    ["All", "Pending", "In Progress", "Resolved"],
                    value="All",
                    label="Status",
                ).props("outlined dense").classes("w-40")
                ui.button("Export CSV", icon="download").props("color=black")

        # Table of reports
        with ui.card().classes(
            "w-full shadow-lg rounded-xl flex-grow flex flex-col"
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
                    "field": "location",
                    "align": "left",
                },
                {
                    "name": "submitted",
                    "label": "Submitted",
                    "field": "submitted",
                    "sortable": True,
                },
                {"name": "status", "label": "Status", "field": "status"},
                {"name": "actions", "label": "Actions", "align": "center"},
            ]

            rows = [
                {
                    "id": "#5821",
                    "category": "Pothole",
                    "location": "Osu, Accra",
                    "submitted": "2024-07-22",
                    "status": "Pending",
                },
                {
                    "id": "#5820",
                    "category": "Sanitation",
                    "location": "East Legon, Accra",
                    "submitted": "2024-07-21",
                    "status": "In Progress",
                },
                {
                    "id": "#5819",
                    "category": "Broken Light",
                    "location": "Madina, Accra",
                    "submitted": "2024-07-20",
                    "status": "Resolved",
                },
            ]

            table = (
                ui.table(columns=columns, rows=rows, row_key="id")
                .classes("w-full")
                .props("flat")
            )

            # Using a lambda function for the slot is a more robust, version-agnostic approach.
            table.add_slot(
                "body-cell-status",
                """
                <q-badge :color="props.row.status === 'Pending' ? 'orange' : (props.row.status === 'In Progress' ? 'blue' : 'green')" class="px-2 py-1 text-xs font-medium">
                    {{ props.row.status }}
                </q-badge>
            """,
            )

            table.add_slot(
                "body-cell-actions",
                """
                <q-td :props="props">
                    <q-btn flat round icon="visibility" @click="() => viewReport(props.row.id)" />
                    <q-btn flat round icon="edit" @click="() => editReport(props.row)" />
                    <q-btn flat round color="negative" icon="delete" @click="() => deleteReport(props.row.id)" />
                </q-td>
            """,
            )

            # Define Python functions to be called from the UI
            def view_report(report_id: str):
                # The report_id from JS will be a string like '#5821'.
                # We can pass it as a query parameter.
                ui.open(f"/view_report?id={report_id.strip('#')}")

            def edit_report(report_data: dict):
                # This would typically open a dialog for editing.
                ui.notify(f"Editing {report_data['id']}")

            def delete_report(report_id: str):
                # This would typically show a confirmation dialog.
                ui.notify(f"Deleting {report_id}", type="negative")

            # Expose the Python functions to JavaScript so they can be called from the @click handlers.
            # This is a more robust way to connect the frontend to the backend.
            ui.add_body_html(f"<script>const viewReport = {view_report}</script>")
            ui.add_body_html(f"<script>const editReport = {edit_report}</script>")
            ui.add_body_html(f"<script>const deleteReport = {delete_report}</script>")
