from nicegui import ui, app
from .sidebar import show_sidebar


@ui.page("/admin/dashboard")
def show_dashboard():
    """Creates the UI for the admin dashboard."""
    # The sidebar must be a top-level element.
    # The main content will automatically be placed to its right.
    show_sidebar()

    # Main content area
    with ui.column().classes("w-full h-full p-8 bg-gray-100 overflow-auto"):
        ui.label("Dashboard").classes("text-4xl font-bold text-gray-800 mb-6")

        # KPI Cards Section
        with ui.row().classes("w-full justify-start gap-6 mb-8"):
            # KPI Card 1: Total Reports
            with ui.link(target="/admin/reports").classes("no-underline"):
                with ui.card().classes(
                    "w-64 p-6 text-center shadow-md hover:shadow-xl transition-shadow"
                ):
                    ui.icon("summarize", size="xl").classes("text-gray-500")
                    ui.label("1,234").classes("text-4xl font-bold mt-2 text-black")
                    ui.label("Total Reports").classes("text-gray-600 font-medium")

            # KPI Card 2: Pending Reports
            with ui.card().classes("w-64 p-6 text-center shadow-md"):
                ui.icon("pending", size="xl").classes("text-orange-500")
                ui.label("56").classes("text-4xl font-bold mt-2 text-orange-600")
                ui.label("Pending Reports").classes("text-gray-600 font-medium")

            # KPI Card 3: Resolved Reports
            with ui.card().classes("w-64 p-6 text-center shadow-md"):
                ui.icon("check_circle", size="xl").classes("text-green-500")
                ui.label("1,178").classes("text-4xl font-bold mt-2 text-green-600")
                ui.label("Resolved Reports").classes("text-gray-600 font-medium")

        # Charts and Recent Activity Section
        with ui.row().classes("w-full gap-6"):
            # Left side: Reports Over Time Chart
            with ui.card().classes("w-2/3 p-6 shadow-md"):
                ui.label("Reports This Week").classes("text-xl font-bold text-gray-700")
                # Using ui.plotly as a replacement for ui.chart for broader version compatibility
                ui.plotly(
                    {
                        "data": [
                            {
                                "x": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                                "y": [5, 7, 3, 8, 4, 6, 2],
                                "name": "Potholes",
                            },
                            {
                                "x": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                                "y": [3, 4, 5, 2, 6, 5, 7],
                                "name": "Sanitation",
                            },
                        ],
                        "layout": {"showlegend": True, "title": False},
                    }
                )

            # Right side: Recent Reports Table
            with ui.card().classes("w-1/3 p-6 shadow-md"):
                ui.label("Recent Activity").classes(
                    "text-xl font-bold text-gray-700 mb-4"
                )
                columns = [
                    {"name": "id", "label": "ID", "field": "id", "align": "left"},
                    {"name": "category", "label": "Category", "field": "category"},
                    {"name": "status", "label": "Status", "field": "status"},
                ]
                rows = [
                    {"id": "#5821", "category": "Pothole", "status": "Pending"},
                    {"id": "#5820", "category": "Sanitation", "status": "Pending"},
                    {
                        "id": "#5819",
                        "category": "Broken Light",
                        "status": "Resolved",
                    },
                    {"id": "#5818", "category": "Theft", "status": "In Progress"},
                ]
                ui.table(columns=columns, rows=rows, row_key="id").props(
                    "flat bordered"
                )
