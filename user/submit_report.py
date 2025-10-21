from nicegui import ui
from sidebar import show_sidebar


@ui.page("/user/submit_report")
def submit_report():
    show_sidebar()
    """Pure UI components for the submit report page."""

    # Assuming 'show_sidebar()' is defined elsewhere and handles its own layout
    # show_sidebar()

    with ui.column().classes("w-full items-center p-10"):
        # Header Section
        ui.label("Report a City Issue").classes("text-4xl font-bold text-gray-800 mb-2")
        ui.label("Help us improve our community by reporting problems.").classes(
            "text-gray-600 mb-10"
        )

        with ui.column().classes("w-full max-w-xl gap-5"):
            # Category Select
            with ui.column().classes("w-full gap-1"):
                ui.label("Category").classes("text-gray-700 font-medium")
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
                ).props("outlined dense").classes("w-full")

            # Title Input
            with ui.column().classes("w-full gap-1"):
                ui.label("Title").classes("text-gray-700 font-medium")
                ui.input("e.g., Large pothole on Main St").props(
                    "outlined dense"
                ).classes("w-full")

            # Description Textarea
            with ui.column().classes("w-full gap-1"):
                ui.label("Description").classes("text-gray-700 font-medium")
                ui.textarea(
                    "Describe the issue in detail, including its size and exact location if possible."
                ).props("outlined dense").classes("w-full")

            # Region/Town Input
            with ui.column().classes("w-full gap-1"):
                ui.label("Region/Town").classes("text-gray-700 font-medium")
                ui.input("e.g., Osu, Accra").props("outlined dense").classes("w-full")

            # GPS Address Input
            with ui.column().classes("w-full gap-1"):
                ui.label("GPS Address").classes("text-gray-700 font-medium")
                ui.input("e.g., GA-435-0123 or a Google Maps link").props(
                    "outlined dense"
                ).classes("w-full")

            # Flyer Upload Component
            with ui.column().classes("w-full gap-1"):
                ui.label("flyer").classes("text-gray-700 font-medium")
                ui.upload(
                    label="Upload a file or drag and drop\nPNG, JPG, GIF up to 10MB",
                ).props("flat bordered color=black").classes("w-full")

            # Submit Button
            ui.button(
                "Submit Report",
            ).classes("w-full max-w-xl py-3 mt-6 text-white bg-black rounded-lg")
