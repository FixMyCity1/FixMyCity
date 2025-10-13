from nicegui import ui, app
from .sidebar import show_sidebar


@ui.page("/admin/dashboard")
def show_dashboard():
    """Creates the UI for the admin dashboard."""
    # The sidebar must be a top-level element.
    # The main content will automatically be placed to its right.
    show_sidebar()

    # Main content area
    with ui.column().classes("w-full h-full p-8 bg-gray-50 overflow-auto"):
        ui.label("Dashboard Overview").classes("text-4xl font-bold text-gray-800 mb-8")

        # KPI Cards Section
        with ui.row().classes(
            "w-full grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8"
        ):
            # KPI Card 1: Total Reports
            with ui.link(target="/admin/reports").classes("no-underline col-span-1"):
                with ui.card().classes(
                    "p-6 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 bg-blue-500 text-white"
                ):
                    with ui.row().classes("w-full items-center justify-between"):
                        with ui.column():
                            ui.label("Total Reports").classes(
                                "text-lg font-medium opacity-80"
                            )
                            ui.label("1,234").classes("text-4xl font-bold")
                        ui.icon("summarize", size="xl").classes("opacity-50")

            # KPI Card 2: Pending Reports
            with ui.link(target="/admin/reports").classes("no-underline col-span-1"):
                with ui.card().classes(
                    "p-6 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 bg-orange-500 text-white"
                ):
                    with ui.row().classes("w-full items-center justify-between"):
                        with ui.column():
                            ui.label("Pending").classes(
                                "text-lg font-medium opacity-80"
                            )
                            ui.label("56").classes("text-4xl font-bold")
                        ui.icon("pending", size="xl").classes("opacity-50")

            # KPI Card 3: Resolved Reports
            with ui.link(target="/admin/reports").classes("no-underline col-span-1"):
                with ui.card().classes(
                    "p-6 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 bg-green-500 text-white"
                ):
                    with ui.row().classes("w-full items-center justify-between"):
                        with ui.column():
                            ui.label("Resolved").classes(
                                "text-lg font-medium opacity-80"
                            )
                            ui.label("1,178").classes("text-4xl font-bold")
                        ui.icon("check_circle", size="xl").classes("opacity-50")

        # Charts and Recent Activity Section
        with ui.row().classes("w-full grid grid-cols-1 lg:grid-cols-3 gap-6"):
            # Left side: Reports Over Time Chart
            with ui.card().classes("lg:col-span-2 p-6 shadow-lg rounded-xl"):
                ui.label("Weekly Report Volume").classes(
                    "text-xl font-bold text-gray-700"
                )
                ui.plotly(
                    {
                        "data": [
                            {
                                "x": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                                "y": [5, 7, 3, 8, 4, 6, 2],
                                "name": "Potholes",
                                "type": "bar",
                                "marker": {"color": "#3b82f6"},
                            },
                            {
                                "x": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                                "y": [3, 4, 5, 2, 6, 5, 7],
                                "name": "Sanitation",
                                "type": "bar",
                                "marker": {"color": "#10b981"},
                            },
                        ],
                        "layout": {
                            "showlegend": True,
                            "title": False,
                            "barmode": "stack",
                            "xaxis": {"gridcolor": "#e5e7eb"},
                            "yaxis": {"gridcolor": "#e5e7eb"},
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "paper_bgcolor": "rgba(0,0,0,0)",
                        },
                    }
                )

            # Right side: Recent Reports Table
            with ui.card().classes("lg:col-span-1 p-6 shadow-lg rounded-xl"):
                ui.label("Recent Activity").classes(
                    "text-xl font-bold text-gray-700 mb-4"
                )
                rows = [
                    {"id": "#5821", "category": "Pothole", "status": "Pending"},
                    {"id": "#5820", "category": "Sanitation", "status": "Pending"},
                    {"id": "#5819", "category": "Broken Light", "status": "Resolved"},
                    {"id": "#5818", "category": "Theft", "status": "In Progress"},
                ]
                with ui.column().classes("gap-4"):
                    for row in rows:
                        with ui.row().classes("w-full items-center"):
                            with ui.column().classes("flex-grow"):
                                ui.label(row["category"]).classes("font-semibold")
                                ui.label(row["id"]).classes("text-sm text-gray-500")
                            ui.badge(
                                row["status"],
                                color={
                                    "Pending": "orange",
                                    "Resolved": "green",
                                    "In Progress": "blue",
                                }.get(row["status"], "gray"),
                            ).classes("px-2 py-1")

                        ui.separator()

                ui.link("View all reports", "/admin/reports").classes(
                    "text-blue-600 hover:underline mt-4 w-full text-center"
                )
