from nicegui import ui, app, run
from sidebar import show_sidebar
import requests
from utils.api import base_url
from typing import List, Dict, Any
from collections import Counter


@ui.page("/auth/analytics")
async def show_analytics():
    """Creates the UI for the reports analytics page."""
    # --- Security Check ---
    role = app.storage.user.get("role")
    if role not in ["admin", "authorities"]:
        ui.notify("You are not authorized to view this page.", type="negative")
        ui.navigate.to("/login")
        return

    show_sidebar()

    async def fetch_analytics_data() -> List[Dict[str, Any]] | None:
        """Fetches all reports from the API for analytics purposes."""
        token = app.storage.user.get("access_token")
        if not token:
            ui.notify("Authentication token not found. Please log in.", type="negative")
            ui.navigate.to("/login")
            return None

        headers = {"Authorization": f"Bearer {token}"}

        def send_request():
            try:
                # Fetch all issues without any filters for a full overview
                return requests.get(f"{base_url}/issues", headers=headers)
            except requests.exceptions.RequestException as e:
                return e

        result = await run.io_bound(send_request)

        if isinstance(result, requests.exceptions.RequestException):
            ui.notify(f"Could not connect to the server: {result}", type="negative")
            return None
        elif result.status_code == 200:
            try:
                json_data = result.json()
                if isinstance(json_data, dict) and "data" in json_data:
                    return json_data["data"]
                elif isinstance(json_data, list):
                    return json_data
                else:
                    ui.notify("API returned unexpected data format.", type="negative")
                    return None
            except requests.exceptions.JSONDecodeError:
                ui.notify("API returned invalid JSON.", type="negative")
                return None
        else:
            ui.notify(f"Error fetching data: {result.text}", type="negative")
            return None

    # Main content area
    with ui.column().classes("w-full h-full p-8 bg-gray-50 overflow-auto"):
        ui.label("Reports Analytics").classes("text-4xl font-bold text-gray-800 mb-8")

        # Show a spinner while data is loading
        spinner = ui.spinner(size="lg").classes("self-center")
        content_area = ui.column().classes("w-full gap-8")
        content_area.set_visibility(False)

        reports_data = await fetch_analytics_data()
        spinner.set_visibility(False)

        if reports_data is None:
            ui.label("Could not load analytics data.").classes("text-red-500")
            return

        content_area.set_visibility(True)
        with content_area:
            # --- KPI Section ---
            status_counts = Counter(report.get("status") for report in reports_data)
            with ui.row().classes("w-full justify-around gap-4"):
                with ui.card().classes("flex-grow text-center p-6"):
                    ui.label("Total Reports").classes("text-lg font-semibold")
                    ui.label(len(reports_data)).classes("text-5xl font-bold")
                with ui.card().classes("flex-grow text-center p-6"):
                    ui.label("Pending").classes("text-lg font-semibold text-orange-600")
                    ui.label(status_counts.get("pending", 0)).classes(
                        "text-5xl font-bold text-orange-600"
                    )
                with ui.card().classes("flex-grow text-center p-6"):
                    ui.label("Completed").classes(
                        "text-lg font-semibold text-green-600"
                    )
                    ui.label(status_counts.get("completed", 0)).classes(
                        "text-5xl font-bold text-green-600"
                    )

            # --- Charts Section ---
            with ui.row().classes("w-full gap-8 mt-8"):
                # Reports by Category (Bar Chart)
                with ui.card().classes("w-1/2 p-4"):
                    ui.label("Reports by Category").classes("text-xl font-bold mb-4")
                    category_counts = Counter(
                        report.get("category", "Uncategorized")
                        for report in reports_data
                    )
                    # Use ui.echart and ECharts-compatible options
                    ui.echart(
                        {
                            "xAxis": {
                                "type": "category",
                                "data": list(category_counts.keys()),
                            },
                            "yAxis": {"type": "value"},
                            "series": [
                                {
                                    "name": "Reports",
                                    "data": list(category_counts.values()),
                                    "type": "bar",
                                }
                            ],
                        }
                    ).classes("w-full")

                # Reports by Status (Pie Chart)
                with ui.card().classes("w-1/2 p-4"):
                    ui.label("Reports by Status").classes("text-xl font-bold mb-4")
                    # Use ui.echart and ECharts-compatible options
                    ui.echart(
                        {
                            "series": [
                                {
                                    "type": "pie",
                                    "data": [
                                        {"value": v, "name": k}
                                        for k, v in status_counts.items()
                                    ],
                                }
                            ],
                        }
                    ).classes("w-full")
