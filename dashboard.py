from nicegui import ui, app, run
from sidebar import show_sidebar
import requests
from utils.api import base_url
from typing import List, Dict, Any


async def _fetch_reports(endpoint: str) -> List[Dict[str, Any]] | None:
    """Generic helper to fetch reports from a given API endpoint."""
    token = app.storage.user.get("access_token")
    if not token:
        ui.notify("Authentication token not found. Please log in.", type="negative")
        ui.navigate.to("/login")
        return None

    headers = {"Authorization": f"Bearer {token}"}

    def send_request():
        try:
            return requests.get(f"{base_url}{endpoint}", headers=headers)
        except requests.exceptions.RequestException as e:
            return e

    result = await run.io_bound(send_request)

    if isinstance(result, requests.exceptions.RequestException):
        ui.notify(f"Could not connect to the server: {result}", type="negative")
        return None
    # Add a check to ensure the result is not None before accessing attributes
    elif result is None:
        ui.notify(
            "Failed to get a response from the server. Please try again.",
            type="negative",
        )
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
                    f"API endpoint '{endpoint}' returned unexpected data format.",
                    type="negative",
                )
                print(
                    f"DEBUG: API response for {endpoint} was not a list or a dict with 'data' key: {json_data}"
                )  # Log for debugging
                return None
        except requests.exceptions.JSONDecodeError:
            ui.notify(
                f"API endpoint '{endpoint}' returned invalid JSON.", type="negative"
            )
            print(
                f"DEBUG: API response for {endpoint} was not valid JSON: {result.text}"
            )  # Log for debugging
            return None
    else:
        ui.notify(
            f"An error occurred while fetching reports: {result.text}", type="negative"
        )
        return None


async def fetch_all_reports_from_api() -> List[Dict[str, Any]] | None:
    """Fetches ALL reports from the API, intended for admins/authorities."""
    return await _fetch_reports("/issues")


async def fetch_user_reports_from_api() -> List[Dict[str, Any]] | None:
    """Fetches reports for the CURRENTLY LOGGED-IN USER from the API."""
    # The backend should use the user's token to filter and return only their own reports from the main /issues endpoint.
    return await _fetch_reports("/issues")


def show_admin_dashboard():
    """Creates the UI for the admin dashboard with full controls."""
    show_sidebar()

    with ui.column().classes("w-full h-full p-8 bg-gray-50 overflow-auto"):
        ui.label("Admin Dashboard Overview").classes(
            "text-4xl font-bold text-gray-800 mb-8"
        )
        # The rest of the admin dashboard UI (KPIs, charts) would go here.
        # For brevity, we'll link directly to the full-featured reports page.
        ui.label(
            "Welcome, Admin. You have full access to manage all reports and users."
        ).classes("text-lg mb-4")
        ui.button(
            "Manage All Reports", on_click=lambda: ui.navigate.to("/admin/reports")
        ).props("color=black")


async def show_authority_dashboard():
    """Creates the UI for an authority to view and update reports."""
    show_sidebar()

    with ui.column().classes("w-full p-8"):
        ui.label("Assigned Reports").classes("text-3xl font-bold mb-6")

        # Define reports_container and spinner outside the rendering loop
        reports_container = ui.column().classes("w-full gap-4")
        spinner = ui.spinner(size="lg").classes("self-center")

        async def load_and_render_authority_reports():
            """Fetches reports and renders them in the reports_container for authorities."""
            spinner.set_visibility(True)
            reports_container.clear()  # Clear existing reports
            reports_data = await fetch_all_reports_from_api()
            spinner.set_visibility(False)

            with reports_container:  # Render new reports inside the container
                if reports_data is None:  # Error case
                    ui.label("Could not load reports.").classes("text-red-500")
                    return
                if not reports_data:
                    ui.label("No reports are currently assigned.").classes(
                        "text-gray-500"
                    )
                    return

                for report in reports_data:
                    with ui.card().classes("w-full p-4"):  # Add padding to the card
                        with ui.row().classes("w-full items-center"):
                            # Info Section - takes up remaining space
                            with ui.column().classes("flex-grow gap-1"):
                                ui.label(report.get("title", "No Title")).classes(
                                    "text-lg font-bold"
                                )
                                ui.label(
                                    f"Location: {report.get('region', 'No Location')}"
                                ).classes("text-sm text-gray-500")
                                # Truncate description to 100 characters
                                description = report.get("description", "")
                                ui.label(
                                    (description[:100] + "...")
                                    if len(description) > 100
                                    else description
                                ).classes("text-sm text-gray-600")

                            # Status and Action Section
                            with ui.column().classes("items-end gap-2"):
                                ui.badge(
                                    report.get("status", "Unknown"),
                                    color={
                                        "Pending": "orange",
                                        "In Progress": "blue",
                                        "Resolved": "green",
                                        "Rejected": "red",
                                    }.get(report.get("status"), "grey"),
                                ).classes("px-3 py-1")
                                ui.button(
                                    "Update Status",
                                    on_click=lambda r=report: ui.navigate.to(
                                        f"/authority/update_report/{r.get('id')}"
                                    ),
                                ).props("flat dense").classes("text-sm")

        # Initial load of reports
        await load_and_render_authority_reports()


async def show_user_dashboard():
    """Creates the UI for a regular user to view their reports."""
    show_sidebar()

    with ui.column().classes("w-full p-8"):
        ui.label("My Submitted Reports").classes("text-3xl font-bold mb-6")

        # Container for the reports list
        user_reports_container = ui.column().classes("w-full gap-4")
        user_spinner = ui.spinner(size="lg").classes("self-center")

        async def load_and_render_user_reports():
            """Fetches reports and renders them in the user_reports_container."""
            user_spinner.set_visibility(True)
            user_reports_container.clear()  # Clear existing reports
            user_reports_data = await fetch_user_reports_from_api()
            user_spinner.set_visibility(False)

            with user_reports_container:  # Render new reports inside the container
                if user_reports_data is None:  # Error case
                    ui.label("Could not load your reports.").classes("text-red-500")
                    return
                if not user_reports_data:
                    ui.label("You haven't submitted any reports yet.").classes(
                        "text-gray-500"
                    )
                    return

                for report in user_reports_data:
                    report_id = report.get("id", "N/A")
                    with ui.card().classes("w-full p-4"):  # Add padding to the card
                        with ui.row().classes("w-full items-center"):
                            # Info Section - takes up remaining space
                            with ui.column().classes("flex-grow gap-1"):
                                # Show Title, Location, and a snippet of the description
                                ui.label(report.get("title", "No Title")).classes(
                                    "text-lg font-bold"
                                )
                                ui.label(
                                    f"Location: {report.get('region', 'No Location')}"
                                ).classes("text-sm text-gray-600")
                                # Truncate description to 100 characters
                                description = report.get("description", "")
                                ui.label(
                                    f'{(description[:100] + "...") if len(description) > 100 else description}'
                                ).classes().classes("text-sm text-gray-500")

                            # Status and Action Section
                            with ui.column().classes("items-end gap-2"):
                                ui.badge(
                                    report.get("status", "Unknown"),
                                    color={
                                        "Pending": "orange",
                                        "In Progress": "blue",
                                        "Resolved": "green",
                                        "Rejected": "red",
                                    }.get(report.get("status"), "grey"),
                                ).classes("px-3 py-1")
                                ui.button(
                                    "View Details",
                                    on_click=lambda r_id=report_id: ui.navigate.to(
                                        f"/view_report/{r_id}"
                                    ),
                                ).props("flat dense").classes("text-sm")

        # Initial load of reports
        await load_and_render_user_reports()


@ui.page("/dashboard")
async def show_dashboard():
    """
    This function acts as a router, displaying the correct dashboard
    based on the user's role stored in the session.
    """
    # In a real app, you would get the role after the user logs in.
    # We'll use a query parameter for demonstration: /dashboard?role=admin
    # A better way is to set it in app.storage.user after login.
    # For example, in your login logic: app.storage.user['role'] = 'admin'
    role = app.storage.user.get("role")

    if not role:
        # If no role is found, redirect to login. This protects the page.
        ui.navigate.to("/login")
        ui.label("Redirecting to login...")
        return

    # Render the dashboard based on the role
    if role == "admin":  # Match lowercase role from backend
        show_admin_dashboard()
    elif role == "authorities":
        await show_authority_dashboard()  # This now calls load_and_render_authority_reports internally
    elif role == "user":  # Match lowercase role from backend
        await show_user_dashboard()  # This now calls load_and_render_user_reports internally
    else:
        # Fallback for unknown roles
        ui.label(f"Unknown role: {role}")
