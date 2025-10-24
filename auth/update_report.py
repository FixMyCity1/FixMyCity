from nicegui import ui, app, run
from sidebar import show_sidebar
import requests
from utils.api import base_url


@ui.page("/authority/update_report/{report_id}")
async def update_report_page(report_id: str):
    """UI for an authority to update a report's status."""

    # --- Security Check ---
    # Ensure the user has the correct role to access this page.
    if app.storage.user.get("role") not in ["authorities", "admin"]:
        ui.notify("You are not authorized to view this page.", type="negative")
        ui.navigate.to("/login")
        return

    show_sidebar()

    async def fetch_report_details(r_id: str):
        """Fetches a single report's details from the API."""
        token = app.storage.user.get("access_token")
        if not token:
            ui.notify("Authentication token not found. Please log in.", type="negative")
            ui.navigate.to("/login")
            return None

        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = await run.io_bound(
                lambda: requests.get(f"{base_url}/issues/{r_id}", headers=headers)
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            json_response = response.json()
            # The API wraps the report object in a 'data' key, so we extract it.
            if isinstance(json_response, dict) and "data" in json_response:
                return json_response["data"]
            # Fallback in case the API returns the object directly in the future.
            return json_response
        except requests.exceptions.RequestException as e:
            ui.notify(f"Error fetching report: {e}", type="negative")
            return None

    with ui.column().classes("w-full p-8"):
        report = await fetch_report_details(report_id)

        if not report:
            ui.label("Report Not Found").classes("text-2xl font-bold text-red-500")
            ui.button(
                "Back to Dashboard", on_click=lambda: ui.navigate.to("/dashboard")
            )
            return

        # --- Report Details Section ---
        ui.label("Update Report Status").classes("text-4xl font-bold text-gray-800")
        ui.label(f"Viewing Report #{report.get('id')}").classes("text-gray-500 mb-6")

        with ui.card().classes("w-full p-6"):
            with ui.row().classes("w-full gap-8"):
                # Left side: Image
                with ui.column().classes("w-1/2"):
                    ui.label("Submitted Photo").classes("text-xl font-bold mb-2")
                    ui.image(
                        report.get(
                            "flyer",
                            "https://placehold.co/800x600/e0e0e0/333?text=No+Image",
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
                            ui.label(
                                f"Category: {report.get('category', 'N/A')}"
                            ).classes("text-lg")
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("location_on", size="sm").classes("text-gray-600")
                            ui.label(f"Location: {report.get('region')}").classes(
                                "text-lg"
                            )
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("my_location", size="sm").classes("text-gray-600")
                            ui.label(f"GPS: {report.get('gps_location')}").classes(
                                "text-lg"
                            )

                    ui.label("Description").classes("text-xl font-bold mt-4 mb-1")
                    ui.label(report.get("description")).classes(
                        "text-gray-700 leading-relaxed"
                    )

        # --- Update Form Section ---
        with ui.card().classes("w-full mt-8 p-6"):
            ui.label("Take Action").classes("text-2xl font-bold mb-4")
            with ui.column().classes("w-full gap-4"):
                # Map the backend status (e.g., 'in-progress') to the frontend display value (e.g., 'In Progress')
                backend_to_frontend_status_map = {
                    "pending": "Pending",
                    "in-progress": "In Progress",
                    "completed": "Resolved",
                    "rejected": "Rejected",
                }
                current_status_for_display = backend_to_frontend_status_map.get(
                    report.get("status"), report.get("status")
                )
                status_select = (
                    ui.select(
                        ["Pending", "In Progress", "Resolved", "Rejected"],
                        label="Update Status",
                        value=current_status_for_display,
                    )
                    .props("outlined dense")
                    .classes("w-full max-w-sm")
                )

                update_comment = (
                    ui.textarea("Add an official comment (optional)")
                    .props("outlined")
                    .classes("w-full")
                )

                async def handle_update():
                    """Handles the API call to update the report status."""
                    # Get the display value from the select component (e.g., "In Progress")
                    selected_status_display = status_select.value

                    # Map the frontend display value to the required backend format
                    frontend_to_backend_status_map = {
                        "Pending": "pending",
                        "In Progress": "in-progress",
                        "Resolved": "completed",
                        "Rejected": "rejected",
                    }
                    new_status_for_backend = frontend_to_backend_status_map.get(
                        selected_status_display, selected_status_display.lower()
                    )

                    token = app.storage.user.get("access_token")
                    headers = {
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }
                    data = {"status_value": new_status_for_backend}

                    def send_request():
                        try:
                            return requests.put(
                                f"{base_url}/issues/{report_id}",
                                data=data,
                                headers=headers,
                            )
                        except requests.exceptions.RequestException as e:
                            return e

                    result = await run.io_bound(send_request)

                    if isinstance(result, requests.exceptions.RequestException):
                        ui.notify(
                            f"Could not connect to the server: {result}",
                            type="negative",
                        )
                    elif result.status_code == 200:
                        ui.notify(
                            f"Report #{report_id} status updated to '{selected_status_display}'.",
                            type="positive",
                        )
                        ui.navigate.to("/dashboard")
                    elif result.status_code == 403:
                        ui.notify(
                            "Authentication error. Please log in again.",
                            type="negative",
                        )
                        ui.navigate.to("/login")
                    elif result.status_code == 422:
                        try:
                            error_detail = result.json()
                            # Display specific validation errors from the backend
                            if "detail" in error_detail:
                                ui.notify(
                                    f"Validation Error: {error_detail['detail']}",
                                    type="warning",
                                )
                            else:
                                ui.notify(
                                    f"Invalid data for status update: {error_detail}",
                                    type="warning",
                                )
                        except:
                            ui.notify(
                                "Invalid data for status update (could not parse error).",
                                type="warning",
                            )

                    else:
                        ui.notify(f"An error occurred: {result.text}", type="negative")

                ui.button("Submit Update", on_click=handle_update).props(
                    "color=black"
                ).classes("w-full max-w-sm py-2")
