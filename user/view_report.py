from nicegui import ui, app, run
import requests
from utils.api import base_url


def create_report_view(report: dict):
    """Creates the UI components for displaying a single report's details."""
    with ui.card().classes("w-full max-w-5xl p-8 shadow-lg rounded-xl"):
        # Report Header
        with ui.row().classes("w-full justify-between items-start"):
            with ui.column().classes("gap-1"):
                ui.label("Report Details").classes("text-4xl font-bold text-black")
            ui.badge(
                report.get("status", "Unknown"),
                color={
                    "Pending": "orange",
                    "In Progress": "blue",
                    "Resolved": "green",
                    "Rejected": "red",
                }.get(report.get("status"), "grey"),
            ).classes("px-4 py-2 text-base")

        ui.separator().classes("my-6")

        # Main Content: Image and Details
        with ui.row().classes("w-full gap-8"):
            # Left side: Image
            with ui.column().classes("w-1/2"):
                ui.label("Submitted Photo").classes("text-xl font-bold mb-2")
                # Assuming the API provides a 'photo_url' field for the image
                ui.image(
                    report.get(
                        "flyer", "https://placehold.co/800x600/e0e0e0/333?text=No+Image"
                    )
                ).classes("w-full rounded-lg shadow-md")

            # Right side: Details
            with ui.column().classes("w-1/2 gap-4"):
                ui.label(report.get("title", "No Title")).classes(
                    "text-3xl font-bold text-gray-800"
                )
                with ui.column().classes("gap-3 mt-2"):
                    with ui.row().classes("items-center gap-3"):
                        ui.icon("category", size="sm").classes("text-gray-600")
                        ui.label(f"Category: {report.get('category', 'N/A')}").classes(
                            "text-lg"
                        )
                    with ui.row().classes("items-center gap-3"):
                        ui.icon("location_on", size="sm").classes("text-gray-600")
                        ui.label(f"Location: {report.get('region', 'N/A')}").classes(
                            "text-lg"
                        )
                    if report.get("created_at"):
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("calendar_today", size="sm").classes(
                                "text-gray-600"
                            )
                            ui.label(f"Submitted: {report.get('created_at')}").classes(
                                "text-lg"
                            )

                ui.label("Description").classes("text-xl font-bold mt-6 mb-1")
                ui.label(report.get("description", "No description provided.")).classes(
                    "text-gray-700 leading-relaxed text-base"
                )

        ui.separator().classes("my-8")

        # Updates Section
        with ui.column().classes("w-full"):
            ui.label("Official Updates").classes("text-2xl font-bold mb-4")
            updates = report.get("updates", [])
            if updates:
                with ui.column().classes("w-full gap-4"):
                    for update in updates:
                        with ui.card().props("bordered").classes("w-full"):
                            with ui.card_section():
                                ui.label(update.get("comment", "No comment.")).classes(
                                    "text-base"
                                )
                                ui.label(update.get("created_at", "")).classes(
                                    "text-sm text-gray-500 mt-1"
                                )
            else:
                ui.label("No official updates have been posted yet.").classes(
                    "text-gray-500"
                )


@ui.page("/view_report/{report_id}")
async def show_view_report(report_id: str):
    """Fetches and displays the details for a single report from the API."""
    ui.query(".nicegui-content").classes("p-0 m-0")

    # --- Security Check ---
    if not app.storage.user.get("role"):
        ui.notify("You must be logged in to view reports.", type="negative")
        ui.navigate.to("/login")
        return

    with ui.column().classes("w-full items-center bg-gray-50 py-12 px-4 min-h-screen"):
        # Add a back button at the top of the page for easy navigation
        with ui.row().classes("w-full max-w-5xl mb-4"):
            ui.button("Back", on_click=ui.navigate.back, icon="arrow_back").props(
                "flat"
            )
        # Show a spinner while data is loading
        spinner = ui.spinner(size="lg").classes("text-black")

        # Fetch data and build the UI
        report = await fetch_report_data(report_id)
        spinner.set_visibility(False)

        if report:
            create_report_view(report)
        else:
            # Show a 'not found' message if the API call failed
            with ui.card().classes("w-full max-w-5xl p-8 shadow-lg rounded-xl"):
                ui.label("Report Not Found or Error Loading").classes(
                    "text-2xl font-bold text-red-500"
                )
                ui.button(
                    "Back to Dashboard", on_click=lambda: ui.navigate.to("/dashboard")
                )


async def fetch_report_data(report_id: str):
    """Performs the API call to get report details."""
    token = app.storage.user.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    def send_request():
        try:
            # Assuming the endpoint is /issues/{id}
            return requests.get(f"{base_url}/issues/{report_id}", headers=headers)
        except requests.exceptions.RequestException as e:
            return e

    result = await run.io_bound(send_request)

    if isinstance(result, requests.exceptions.RequestException):
        ui.notify(f"Could not connect to the server: {result}", type="negative")
        return None
    elif result.status_code == 200:
        json_response = result.json()
        # The API wraps the report object in a 'data' key, so we extract it.
        if isinstance(json_response, dict) and "data" in json_response:
            return json_response["data"]
        # Fallback in case the API returns the object directly in the future.
        return json_response
    elif result.status_code == 404:
        ui.notify("Report not found.", type="warning")
        return None
    elif result.status_code == 403:
        ui.notify("Authentication error. Please log in again.", type="negative")
        ui.navigate.to("/login")
        return None
    else:
        ui.notify(f"An error occurred: {result.text}", type="negative")
        return None
