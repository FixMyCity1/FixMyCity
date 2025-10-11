from nicegui import ui, app
from .sidebar import show_sidebar


@ui.page("/admin/reports")
def show_reports():
    """Creates the UI for the admin reports management page."""
    # The sidebar must be a top-level element.
    # The main content will automatically be placed to its right.
    show_sidebar()

    # Main content area
    with ui.column().classes("w-full h-full p-8 bg-gray-100 overflow-auto"):
        ui.label("Manage Reports").classes("text-4xl font-bold text-gray-800 mb-6")

        # Table of reports
        with ui.card().classes("w-full p-6 shadow-md"):
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

            table = ui.table(columns=columns, rows=rows, row_key="id").classes("w-full")

            # Using a lambda function for the slot is a more robust, version-agnostic approach.
            table.add_slot(
                "body-cell-status",
                """
                <q-badge :color="props.row.status === 'Pending' ? 'orange' : (props.row.status === 'In Progress' ? 'blue' : 'green')">
                    {{ props.row.status }}
                </q-badge>
            """,
            )

            with table.add_slot("body-cell-actions") as slot:
                status_colors = {
                    "Pending": "orange",
                    "In Progress": "blue",
                    "Resolved": "green",
                }
                ui.button(icon="visibility", on_click=lambda: ui.notify("View")).props(
                    "flat round"
                )
                ui.button(icon="edit", on_click=lambda: ui.notify("Edit")).props(
                    "flat round"
                )
