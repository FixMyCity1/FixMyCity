from nicegui import ui


def show_header():
    with ui.header().style(
        "background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); box-shadow: none;"
    ):
        with ui.row().classes("w-full justify-between items-center px-8"):
            with ui.row().classes("items-center gap-2"):
                ui.icon("location_city").classes("text-3xl text-sky-500")
                ui.label("FixMyCity").classes("text-2xl font-bold text-sky-500")

            with ui.row().classes("gap-4 items-center"):
                ui.link("Report an Issue").classes(
                    "text-lg font-bold text-sky-500 hover:text-black transition-colors no-underline"
                )
                ui.link("login").classes(
                    "text-lg font-bold text-sky-500 hover:text-black transition-colors no-underline"
                )
                ui.link("Sign Up").classes(
                    "auth-btn rounded-xl px-3 py-2 no-underline font-bold tracking-widest leading-tight"
                ).style(
                    "background:#0284c7 !important; color:white; letter-spacing: 0.15em; align-items:center;"
                )
