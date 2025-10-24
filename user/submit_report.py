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

    with ui.column().classes("w-full items-center p-4 sm:p-8 bg-gray-100 min-h-screen"):
        with ui.card().classes("w-full max-w-2xl p-8 shadow-lg rounded-xl"):
            ui.label("Report a City Issue").classes(
                "text-4xl font-bold text-gray-800 mb-2"
            )
            ui.label("Help us improve our community by reporting problems.").classes(
                "text-gray-600 mb-8"
            )

            # --- Issue Details Section ---
            ui.label("1. What is the issue?").classes("text-xl font-semibold mt-4 mb-2")
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
                    label="Category",
                    with_input=True,
                )
                .props("outlined")
                .classes("w-full")
            )
            title = (
                ui.input(label="Title", placeholder="e.g., Large pothole on Main St")
                .props("outlined")
                .classes("w-full")
            )
            description = (
                ui.textarea(
                    label="Description", placeholder="Describe the issue in detail..."
                )
                .props("outlined")
                .classes("w-full")
            )

            # --- Location Section ---
            ui.label("2. Where is the issue located?").classes(
                "text-xl font-semibold mt-6 mb-2"
            )
            region = (
                ui.input(label="Region / Area", placeholder="e.g., Osu, Accra")
                .props("outlined")
                .classes("w-full")
            )
            gps_location = (
                ui.input(
                    label="GPS Address or Landmark",
                    placeholder="e.g., GA-435-0123 or near the post office",
                )
                .props("outlined")
                .classes("w-full")
            )

            # --- Photo Upload Section ---
            ui.label("3. Add a photo").classes("text-xl font-semibold mt-6 mb-2")

            flyer = (
                ui.upload(
                    label="Take or Upload a Photo (PNG, JPG up to 10MB)",
                    multiple=False,
                    max_file_size=10_000_000,
                )
                .props('flat bordered color=black capture="environment"')
                .classes("w-full mb-2")
            )

            # --- Submit Handler ---
            def handle_submit_ui_only():
                ui.notify("Report submitted (UI simulation only)!", type="positive")

            ui.button("Submit Report", on_click=handle_submit_ui_only).props(
                "color=black size=lg"
            ).classes("w-full py-3 mt-6 rounded-lg")
