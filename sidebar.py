from nicegui import ui, app


def _create_sidebar_footer():
    """Creates the common footer for all sidebars with user info and logout."""
    with ui.column().classes("w-full"):
        ui.separator().classes("bg-gray-700")
        with ui.row().classes("w-full p-4 items-center gap-4"):
            ui.icon("account_circle", size="lg").classes("text-gray-400")
            with ui.column().classes("gap-0"):
                # Dynamically display user info from session
                role = app.storage.user.get("role", "Guest")
                email = app.storage.user.get("email", "guest@example.com")
                ui.label(role).classes("font-semibold")
                ui.label(email).classes("text-sm text-gray-400")

            def handle_logout():
                app.storage.user.clear()
                ui.navigate.to("/login")

            ui.button(icon="logout", on_click=handle_logout).props(
                "flat round color=white"
            )


def show_admin_sidebar():
    """The sidebar for administrators with full access."""
    with ui.left_drawer().classes("bg-gray-900 text-white").props(
        "width=280"
    ) as sidebar:
        with ui.column().classes("h-full w-full justify-between no-wrap"):
            with ui.column().classes("w-full"):
                with ui.row().classes("p-4 w-full items-center justify-center"):
                    ui.icon("admin_panel_settings", size="lg").classes("text-gray-400")
                    ui.label("Admin Panel").classes("text-2xl font-bold")
                ui.separator().classes("bg-gray-700")
                with ui.column().classes("w-full p-4 gap-2"):
                    ui.link("Dashboard", "/dashboard").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
                    ui.link("Reports", "/admin/reports").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
            _create_sidebar_footer()


def show_authority_sidebar():
    """The sidebar for authorities who manage reports."""
    with ui.left_drawer().classes("bg-gray-900 text-white").props(
        "width=280"
    ) as sidebar:
        with ui.column().classes("h-full w-full justify-between no-wrap"):
            with ui.column().classes("w-full"):
                with ui.row().classes("p-4 w-full items-center justify-center"):
                    ui.icon("gavel", size="lg").classes("text-gray-400")
                    ui.label("Authority Portal").classes("text-2xl font-bold")
                ui.separator().classes("bg-gray-700")
                with ui.column().classes("w-full p-4 gap-2"):
                    ui.link("Assigned Reports", "/dashboard").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
            _create_sidebar_footer()


def show_user_sidebar():
    """The sidebar for regular users."""
    with ui.left_drawer().classes("bg-gray-900 text-white").props(
        "width=280"
    ) as sidebar:
        with ui.column().classes("h-full w-full justify-between no-wrap"):
            with ui.column().classes("w-full"):
                with ui.row().classes("p-4 w-full items-center justify-center"):
                    ui.icon("dashboard", size="lg").classes("text-gray-400")
                    ui.label("My Dashboard").classes("text-2xl font-bold")
                ui.separator().classes("bg-gray-700")
                with ui.column().classes("w-full p-4 gap-2"):
                    ui.link("My Reports", "/dashboard").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
                    ui.link("Submit New Report", "/user/submit_report").classes(
                        "w-full text-lg text-white no-underline hover:bg-gray-700 p-2 rounded-md transition-colors"
                    )
            _create_sidebar_footer()


def show_sidebar():
    """
    Acts as a router to display the correct sidebar based on the user's role.
    """
    role = app.storage.user.get("role")

    if role == "Administrator":
        show_admin_sidebar()
    elif role == "Authority":
        show_authority_sidebar()
    elif role == "User":
        show_user_sidebar()
    # If no role is found (e.g., user not logged in), no sidebar will be shown.
