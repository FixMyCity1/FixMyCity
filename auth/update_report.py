from nicegui import ui, app
from sidebar import show_sidebar

# In a real application, you would import your database module
# import database

# --- Mock Data (for demonstration) ---
# This would be replaced by a call like `database.get_report_by_id(report_id)`
MOCK_REPORTS = {
    "5821": {
        "id": "5821",
        "title": "Large Pothole on Main St",
        "category": "Pothole",
        "location": "Osu, Accra",
        "gps_address": "GA-123-4567",
        "description": "A very large and deep pothole has formed in the middle of the road, causing traffic issues and potential damage to vehicles. It has been growing for the past two weeks.",
        "photo_path": "https://placehold.co/800x600/e0e0e0/333?text=Pothole",
        "status": "Pending",
        "submitted_on": "July 22, 2024",
    },
    "5820": {
        "id": "5820",
        "title": "Waste Overflowing from Bins",
        "category": "Sanitation",
        "location": "East Legon, Accra",
        "gps_address": "GA-456-7890",
        "description": "Public waste bins have not been collected for over a week and are now overflowing onto the street, creating a health hazard.",
        "photo_path": "https://placehold.co/800x600/e0e0e0/333?text=Sanitation",
        "status": "In Progress",
        "submitted_on": "July 21, 2024",
    },
}


@ui.page("/authority/update_report/{report_id}")
def update_report_page(report_id: str):
    """UI for an authority to update a report's status."""

    # --- Security Check ---
    # Ensure the user has the correct role to access this page.
    if app.storage.user.get("role") != "Authority":
        ui.notify("You are not authorized to view this page.", type="negative")
        ui.navigate.to("/login")
        return

    show_sidebar()

    # Fetch the report data (using mock data for now)
    report = MOCK_REPORTS.get(report_id)

    with ui.column().classes("w-full p-8"):
        if not report:
            ui.label("Report Not Found").classes("text-2xl font-bold text-red-500")
            ui.button(
                "Back to Dashboard", on_click=lambda: ui.navigate.to("/dashboard")
            )
            return

        # --- Report Details Section ---
        ui.label("Update Report Status").classes("text-4xl font-bold text-gray-800")
        ui.label(f"Viewing Report #{report['id']}").classes("text-gray-500 mb-6")

        with ui.card().classes("w-full p-6"):
            with ui.row().classes("w-full gap-8"):
                # Left side: Image
                with ui.column().classes("w-1/2"):
                    ui.label("Submitted Photo").classes("text-xl font-bold mb-2")
                    ui.image(report["photo_path"]).classes(
                        "w-full rounded-lg shadow-md"
                    )

                # Right side: Details
                with ui.column().classes("w-1/2 gap-4"):
                    ui.label(report["title"]).classes(
                        "text-3xl font-bold text-gray-800"
                    )
                    with ui.column().classes("gap-3 mt-2"):
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("category", size="sm").classes("text-gray-600")
                            ui.label(f"Category: {report['category']}").classes(
                                "text-lg"
                            )
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("location_on", size="sm").classes("text-gray-600")
                            ui.label(f"Location: {report['location']}").classes(
                                "text-lg"
                            )
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("my_location", size="sm").classes("text-gray-600")
                            ui.label(f"GPS: {report['gps_address']}").classes("text-lg")

                    ui.label("Description").classes("text-xl font-bold mt-4 mb-1")
                    ui.label(report["description"]).classes(
                        "text-gray-700 leading-relaxed"
                    )

        # --- Update Form Section ---
        with ui.card().classes("w-full mt-8 p-6"):
            ui.label("Take Action").classes("text-2xl font-bold mb-4")
            with ui.column().classes("w-full gap-4"):
                status_select = (
                    ui.select(
                        ["Pending", "In Progress", "Resolved", "Rejected"],
                        label="Update Status",
                        value=report["status"],
                    )
                    .props("outlined dense")
                    .classes("w-full max-w-sm")
                )

                update_comment = (
                    ui.textarea("Add an official comment (optional)")
                    .props("outlined")
                    .classes("w-full")
                )

                def handle_update():
                    new_status = status_select.value
                    # In a real app, you would save this to the database:
                    # database.update_report_status(report_id, new_status, update_comment.value)
                    ui.notify(
                        f"Report #{report['id']} status updated to '{new_status}'.",
                        type="positive",
                    )
                    ui.navigate.to("/dashboard")

                ui.button("Submit Update", on_click=handle_update).props(
                    "color=black"
                ).classes("w-full max-w-sm py-2")
