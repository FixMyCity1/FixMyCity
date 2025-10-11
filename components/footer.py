from nicegui import ui
import datetime


def show_footer():
    """Displays a comprehensive footer for the website."""
    with ui.element("footer").classes("w-full bg-gray-900 text-white pt-16 pb-8 px-8"):
        with ui.row().classes("w-full justify-around gap-8"):
            # Column 1: Branding and About
            with ui.column().classes("w-full md:w-1/4"):
                ui.label("FixMyCity").classes("text-3xl font-bold mb-2")
                ui.label(
                    "Empowering citizens to build cleaner, safer, and more sustainable cities in Ghana."
                ).classes("text-gray-300 text-base")

            # Column 2: Quick Links
            with ui.column().classes("gap-1"):
                ui.label("Navigate").classes("text-lg font-semibold mb-2")
                ui.label("Home").classes("text-gray-300")
                ui.label("About Us").classes("text-gray-300")
                ui.label("Public Feed").classes("text-gray-300")
                ui.label("Blog").classes("text-gray-300")

            # Column 3: Contact Us
            with ui.column().classes("gap-1"):
                ui.label("Contact Us").classes("text-lg font-semibold mb-2")
                with ui.row().classes("items-center gap-2"):
                    ui.icon("location_on", color="white")
                    ui.label("123 Agri Lane, Accra, Ghana").classes("text-gray-300")
                with ui.row().classes("items-center gap-2"):
                    ui.icon("email", color="white")
                    ui.label("contact@fixmycity.com.gh").classes("text-gray-300")

            # Column 4: Social Media
            with ui.column().classes("gap-2 items-start"):
                ui.label("Follow Us").classes("text-lg font-semibold")
                with ui.row().classes("gap-2"):
                    ui.icon("fab fa-twitter").classes("text-2xl p-2 rounded-full")
                    ui.icon("fab fa-facebook-f").classes("text-2xl p-2 rounded-full")
                    ui.icon("fab fa-linkedin-in").classes("text-2xl p-2 rounded-full")

        ui.separator().classes("my-8 bg-gray-700")

        with ui.row().classes("w-full justify-between items-center"):
            ui.label(
                f"© {datetime.date.today().year} FixMyCity. All Rights Reserved."
            ).classes("text-gray-400")
            with ui.row().classes("gap-4"):
                ui.label("Privacy Policy").classes("text-gray-400")
                ui.label("Terms of Service").classes("text-gray-400")
