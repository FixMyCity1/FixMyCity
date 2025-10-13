from nicegui import ui, app


@ui.page("/login")
def show_login():
    ui.query(".nicegui-content").classes("m-0 p-0")
    with ui.row().classes("w-full h-screen m-0 p-0 gap-0"):
        # Left side signin form
        with ui.column().classes(
            "w-2/5 h-full justify-center items-center bg-white p-10"
        ):
            ui.label("login").classes("text-3xl font-bold mb-6")

            # Input fields
            email = ui.input("Email").classes("w-80 mb-4")
            password = ui.input(
                "Password", password=True, password_toggle_button=True
            ).classes("w-80 mb-6")

            # Signin button
            ui.button("Sign In").classes("w-80 bg-black text-white py-2 rounded-lg")

            # Link to signup
            with ui.row().classes("mt-4 items-center"):
                ui.label("Don't have an account?").classes("text-gray-600")
                ui.link("Sign up here", "/signup").classes(
                    "text-black hover:underline ml-1"
                )

        # Right side image
        with ui.element("div").classes("w-3/5 h-full relative"):
            ui.image("/assets/login2.jpg").classes(
                "w-full h-full object-cover rounded-lg shadow-lg"
            )
            with ui.column().classes(
                "absolute inset-0 bg-black/40 bg-opacity-40 flex justify-end p-12 text-white"
            ):
                ui.label("FixMyCity").classes("text-5xl font-bold")
                ui.label(
                    "Your voice for a better community. Report issues, see results."
                ).classes("text-2xl text-gray-200 mt-2")
