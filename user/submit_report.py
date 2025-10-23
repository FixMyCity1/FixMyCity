from nicegui import ui, app
from sidebar import show_sidebar


@ui.page("/user/submit_report")
def submit_report():
    # --- Security Check ---
    # Redirect to login if the user is not authenticated. This is necessary
    # for the sidebar to know which version to display.
    if not app.storage.user.get("role"):
        ui.notify("You must be logged in to submit a report.", type="negative")
        ui.navigate.to("/login")
        return

    # Display the sidebar for the logged-in user
    show_sidebar()

    with ui.column().classes("w-full items-center p-8 bg-gray-50 min-h-screen"):
        ui.label("Report a City Issue").classes("text-4xl font-bold text-gray-800 mb-2")
        ui.label("Help us improve our community by reporting problems.").classes(
            "text-gray-600 mb-10"
        )

        # Input fields
        category = (
            ui.select(
                [
                    "Potholes",
                    "Waste Management",
                    "Water Supply",
                    "Electricity Outage",
                    "Roads & Traffic",
                    "Public Safety",
                    "Illegal Construction",
                    "Environmental Pollution",
                    "Other",
                ],
                label="Select a category",
            )
            .props("outlined dense")
            .classes("w-full max-w-xl")
        )

        title = (
            ui.input("e.g., Large pothole on Main St")
            .props("outlined dense")
            .classes("w-full max-w-xl")
        )
        description = (
            ui.textarea("Describe the issue in detail...")
            .props("outlined dense")
            .classes("w-full max-w-xl")
        )
        region = (
            ui.input("e.g., Osu, Accra")
            .props("outlined dense")
            .classes("w-full max-w-xl")
        )
        gps_address = (
            ui.input("e.g., GA-435-0123 or Google Maps link")
            .props("outlined dense")
            .classes("w-full max-w-xl")
        )

        # Label to provide feedback on file upload
        upload_feedback = ui.label("").classes("text-green-500 text-sm ml-2 hidden")

        def handle_file_upload(e):
            """Handles the file upload event, storing content, name, and MIME type."""
            try:
                upload_feedback.text = f"File selected: {e.name}"
                upload_feedback.classes(remove="hidden")
                ui.notify(f"File '{e.name}' selected.", type="positive")
            except Exception as ex:
                ui.notify(f"Error processing file: {ex}", type="negative")
                upload_feedback.classes(add="hidden")

        flyer_upload = (
            ui.upload(
                label="Upload a file (PNG, JPG, GIF up to 10MB)",
                multiple=False,
                max_file_size=10_000_000,
            )
            .props("flat bordered color=black")
            .on_upload(handle_file_upload)  # Assign the handler here
            .classes("w-full max-w-xl mb-2")
        )

        # --- Submit Handler ---
        def handle_submit_ui_only():
            ui.notify("Report submitted (UI simulation only)!", type="positive")

        ui.button("Submit Report", on_click=handle_submit_ui_only).classes(
            "w-full max-w-xl py-3 mt-6 text-white bg-black rounded-lg"
        )
