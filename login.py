from nicegui import ui, app


@ui.page("/login")
def show_login():
    with ui.row().classes("w-full h-screen m-0 p-0 gap-0"):
        # Left side signin form
        with ui.column().classes(
            "w-1/2 h-full justify-center items-center bg-gray-100 p-10"
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
        ui.image("/assets/signup.jpg").classes("w-1/2 h-full object-cover")
