from nicegui import ui


def show_header():
    with ui.header().style(
        "background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); box-shadow: none;"
    ):
        with ui.row().classes("w-full justify-between items-center px-8"):
            with ui.row().classes("items-center gap-2"):
                ui.icon("location_city").classes("text-3xl text-black")
                ui.label("FixMyCity").classes("text-2xl font-bold text-black")

            with ui.row().classes("gap-4 items-center"):
                ui.link("Report an Issue", "/admin/dashboard").classes(
                    "text-lg font-bold text-black hover:text-gray-600 transition-colors no-underline"
                )
                ui.link("login", "/login").classes(
                    "text-lg font-bold text-black hover:text-gray-600 transition-colors no-underline"
                )
                ui.link("signup", "/signup").classes(
                    "auth-btn rounded-xl px-3 py-2 no-underline font-bold tracking-widest leading-tight"
                ).style(
                    "background:black !important; color:white; letter-spacing: 0.15em; align-items:center;"
                )
