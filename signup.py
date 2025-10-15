from nicegui import ui, app


@ui.page("/signup")
def show_signup():
    ui.query(".nicegui-content").classes("m-0 p-0")
    with ui.row().classes("w-full h-screen m-0 p-0 gap-0"):
        # Left side image
        with ui.element("div").classes("w-3/5 h-full relative"):
            ui.image("/assets/signup.jpg").classes("w-full h-full object-cover")
            with ui.column().classes(
                "absolute inset-0 bg-black/40 flex justify-end p-12 text-white"
            ):
                ui.label("Akwaaba!").classes("text-5xl font-bold")
                ui.label(
                    "Join the movement to build a better Ghana, one report at a time."
                ).classes("text-2xl text-gray-200 mt-2")

        # Right side signup form
        with ui.column().classes(
            "w-2/5 h-full justify-center items-center bg-white p-10"
        ):
            ui.label("Sign Up").classes("text-3xl font-bold mb-6")

            # Input fields
            ui.input("Full Name").classes("w-80 mb-4")
            ui.input("Email").classes("w-80 mb-4")
            ui.input("Password", password=True, password_toggle_button=True).classes(
                "w-80 mb-4"
            )
            ui.input(
                "Confirm Password", password=True, password_toggle_button=True
            ).classes("w-80 mb-4")

            # Role selection
            role = ui.select(
                ["User", "Authority"],
                label="Select Role",
                value="User",
            ).classes("w-80 mb-6")

            # Signup button
            def handle_signup():
                ui.notify(f"Signed up as {role.value or 'Unknown'}")

            ui.button("Sign Up", on_click=handle_signup).classes(
                "w-80 bg-black text-white py-2 rounded-lg"
            )

            # Link to login
            ui.label("Already have an account?").classes("mt-4 text-gray-600")
            ui.link("Sign In", "/login").classes("text-black hover:underline")
