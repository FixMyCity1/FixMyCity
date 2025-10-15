from nicegui import ui, app


@ui.page("/user/submit_report")
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
                category = (
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
                    )
                    .props("outlined dense")
                    .classes("w-full")
                )

            with ui.column().classes("w-full gap-1"):
                ui.label("Title").classes("text-gray-700 font-medium")
                title = (
                    ui.input("e.g., Large pothole on Main St")
                    .props("outlined dense")
                    .classes("w-full")
                )

            with ui.column().classes("w-full gap-1"):
                ui.label("Description").classes("text-gray-700 font-medium")
                description = (
                    ui.textarea(
                        "Describe the issue in detail, including its size and exact location if possible."
                    )
                    .props("outlined dense")
                    .classes("w-full")
                )

            with ui.column().classes("w-full gap-1"):
                ui.label("Region/Town").classes("text-gray-700 font-medium")
                region = (
                    ui.input("e.g., Osu, Accra")
                    .props("outlined dense")
                    .classes("w-full")
                )

            with ui.column().classes("w-full gap-1"):
                ui.label("GPS Address").classes("text-gray-700 font-medium")
                gps_address = (
                    ui.input("e.g., GA-435-0123 or a Google Maps link")
                    .props("outlined dense")
                    .classes("w-full")
                )

            with ui.column().classes("w-full gap-1"):
                ui.label("Photo").classes("text-gray-700 font-medium")
                photo = (
                    ui.upload(
                        label="Upload a file or drag and drop\nPNG, JPG, GIF up to 10MB"
                    )
                    .props("flat bordered color=black")
                    .classes("w-full")
                )

        async def handle_submit():
            # Check if all fields are filled
            if not all(
                [
                    category.value,
                    title.value,
                    description.value,
                    region.value,
                    gps_address.value,
                ]
            ):
                ui.notify("Please fill out all text fields.", type="negative")
                return

            # Check if a file has been uploaded
            if not photo.files:
                ui.notify("Please upload a photo of the issue.", type="negative")
                return

            ui.notify("Report submitted successfully!", type="positive")
            ui.navigate.to("/dashboard")  # Navigate to the user's dashboard

        # Submit Button
        ui.button(
            "Submit Report",
            on_click=handle_submit,
        ).classes("w-full max-w-xl py-3 mt-6 text-white bg-black rounded-lg")
