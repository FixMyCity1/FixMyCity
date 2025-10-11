from nicegui import ui, app
from components.header import show_header
from components.footer import show_footer


@ui.page("/view_report")
def show_view_report():
    """Creates the UI for viewing a single report's details."""
    ui.query(".nicegui-content").classes("p-0 m-0")
    show_header()

    with ui.column().classes("w-full items-center bg-gray-50 py-12 px-4 min-h-screen"):
        with ui.card().classes("w-full max-w-5xl p-8 shadow-lg rounded-xl"):
            # Report Header
            with ui.row().classes("w-full justify-between items-start"):
                with ui.column().classes("gap-1"):
                    ui.label("Report Details").classes("text-4xl font-bold text-black")
                    ui.label("Report ID: #GH-12345").classes("text-gray-500")
                ui.badge("In Progress", color="orange").classes("px-4 py-2 text-base")

            ui.separator().classes("my-6")

            # Main Content: Image and Details
            with ui.row().classes("w-full gap-8"):
                # Left side: Image
                with ui.column().classes("w-1/2"):
                    ui.label("Submitted Photo").classes("text-xl font-bold mb-2")
                    ui.image(
                        "https://placehold.co/800x600/e0e0e0/333?text=Pothole"
                    ).classes("w-full rounded-lg shadow-md")

                # Right side: Details
                with ui.column().classes("w-1/2 gap-4"):
                    ui.label("Large pothole on Main St").classes(
                        "text-3xl font-bold text-gray-800"
                    )

                    # Metadata
                    with ui.column().classes("gap-3 mt-2"):
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("category", size="sm").classes("text-gray-600")
                            ui.label("Category: Pothole").classes("text-lg")
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("location_on", size="sm").classes("text-gray-600")
                            ui.label(
                                "Location: In front of 123 Main St, Osu, Accra"
                            ).classes("text-lg")
                        with ui.row().classes("items-center gap-3"):
                            ui.icon("calendar_today", size="sm").classes(
                                "text-gray-600"
                            )
                            ui.label("Submitted: July 20, 2024").classes("text-lg")

                    # Description
                    ui.label("Description").classes("text-xl font-bold mt-6 mb-1")
                    ui.label(
                        "A very large and deep pothole has formed in the middle of the road, causing traffic issues and potential damage to vehicles. It has been growing for the past two weeks."
                    ).classes("text-gray-700 leading-relaxed text-base")

            ui.separator().classes("my-8")

            # Updates Section
            with ui.column().classes("w-full"):
                ui.label("Official Updates").classes("text-2xl font-bold mb-4")
                with ui.column().classes("w-full gap-4"):
                    # Update 1
                    with ui.card().props("bordered").classes("w-full"):
                        with ui.card_section():
                            ui.label(
                                "Report received and assigned to the Department of Urban Roads."
                            ).classes("text-base")
                            ui.label("July 21, 2024 - 10:30 AM").classes(
                                "text-sm text-gray-500 mt-1"
                            )
                    # Update 2
                    with ui.card().props("bordered").classes("w-full"):
                        with ui.card_section():
                            ui.label(
                                "An inspection team has been dispatched to assess the damage."
                            ).classes("text-base")
                            ui.label("July 22, 2024 - 09:00 AM").classes(
                                "text-sm text-gray-500 mt-1"
                            )

    show_footer()
