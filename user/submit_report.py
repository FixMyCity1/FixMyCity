from nicegui import ui, app


@ui.page("/submit_report")
def submit_report_page():
    with ui.column().classes("w-full items-center justify-center p-10 min-h-screen"):

        # Header Section
        ui.label("Report a City Issue").classes("text-4xl font-bold text-gray-800 mb-2")
        ui.label("Help us improve our community by reporting problems.").classes(
            "text-gray-600 mb-10"
        )

        # Form fields are now directly on the page, constrained by this column
        with ui.column().classes("w-full max-w-xl gap-5"):
            with ui.column().classes("w-full gap-1"):
                ui.label("Category").classes("text-gray-700 font-medium")
                ui.select(
                    [
                        "Sanitation",
                        "Pothole",
                        "Broken Light",
                        "Water Leak",
                        "Drug Abuse",
                        "Theft",
                        "Other",
                    ],
                    label="Select a category",
                ).props("outlined dense").classes("w-full")

            with ui.column().classes("w-full gap-1"):
                ui.label("Title").classes("text-gray-700 font-medium")
                ui.input("e.g., Large pothole on Main St").props(
                    "outlined dense"
                ).classes("w-full")

            with ui.column().classes("w-full gap-1"):
                ui.label("Description").classes("text-gray-700 font-medium")
                ui.textarea(
                    "Describe the issue in detail, including its size and exact location if possible."
                ).props("outlined dense").classes("w-full")

            with ui.column().classes("w-full gap-1"):
                ui.label("Location").classes("text-gray-700 font-medium")
                ui.input("e.g., In front of 123 Main St").props(
                    "outlined dense"
                ).classes("w-full")

            with ui.column().classes("w-full gap-1"):
                ui.label("Photo (Optional)").classes("text-gray-700 font-medium")
                ui.upload(
                    label="Upload a file or drag and drop\nPNG, JPG, GIF up to 10MB"
                ).props("flat bordered color=black").classes("w-full")

        def handle_submit():
            ui.notify("submit successfully")
            ui.navigate.to("/view_report")

        # Submit Button
        ui.button(
            "Submit Report",
            on_click=handle_submit,
        ).classes("w-full max-w-xl py-3 mt-6 text-white bg-black rounded-lg")
