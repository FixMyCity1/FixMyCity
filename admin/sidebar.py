from nicegui import ui, app


def show_sidebar():
    """Creates a reusable admin sidebar with navigation links."""
    with ui.left_drawer().classes("bg-gray-900 text-white").props(
        "width=280"
    ) as sidebar:
        with ui.column().classes("h-full w-full justify-between no-wrap"):
            # Top Section: Title and Navigation
            with ui.column().classes("w-full"):
                # Admin Panel Title
                with ui.row().classes("p-4 w-full items-center justify-center"):
                    ui.icon("admin_panel_settings", size="lg").classes("text-gray-400")
                    ui.label("Admin Panel").classes("text-2xl font-bold")

                ui.separator().classes("bg-gray-700")

                # Navigation Links
                with ui.column().classes("w-full p-4 gap-2"):
                    # Using ui.link for direct navigation
                    ui.link("Dashboard", "/admin/dashboard").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
                    ui.link("Reports", "/admin/reports").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
                    ui.link("Analytics", "/admin/analytics").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
                    ui.link("Users").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )

            # Bottom Section: User Profile and Logout
            with ui.column().classes("w-full"):
                ui.separator().classes("bg-gray-700")
                with ui.row().classes("w-full p-4 items-center gap-4"):
                    ui.icon("account_circle", size="lg").classes("text-gray-400")
                    with ui.column().classes("gap-0"):
                        ui.label("Admin User").classes("font-semibold")
                        ui.label("admin@fixmycity.com").classes("text-sm text-gray-400")
                    ui.button(
                        icon="logout", on_click=lambda: ui.navigate.to("/login")
                    ).props("flat round color=white")
