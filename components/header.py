from nicegui import ui


def show_header():
    with ui.header().style(
        "background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); box-shadow: none;"
    ):
        with ui.row().classes("w-full justify-between items-center px-8"):
            with ui.row().classes("items-center gap-2"):
                ui.icon("agriculture").classes("text-3xl text-green-500")
                ui.label("Agrimo").classes("text-2xl font-bold text-green-500")

            with ui.row().classes("gap-4 items-center"):
                ui.link("Login").classes(
                    "text-lg font-bold uppercase text-green-500 hover:text-white transition-colors"
                )
                ui.link("Sign Up").classes(
                    "auth-btn uppercase rounded-xl px-3 py-2 no-underline font-bold tracking-widest leading-tight"
                ).style(
                    "background:#2e7d32 !important; color:white; letter-spacing: 0.15em; align-items:center;"
                )
