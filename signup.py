from nicegui import ui, app


@ui.page("/signup")
def show_signup():
    with ui.row().classes("w-full h-screen m-0 p-0 gap-0"):
        # Left side image
        ui.image("").classes("w-1/2 h-full object-cover")

        # Right side signup form
        with ui.column().classes(
            "w-1/2 h-full justify-center items-center bg-gray-100 p-10"
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
            role = ui.select(["User", "Admin"], label="Select Role").classes(
                "w-80 mb-6"
            )

            # Signup button
            def handle_signup():
                ui.notify(f"Signed up as {role.value or 'Unknown'}")

            ui.button("Sign Up", on_click=handle_signup).classes(
                "w-80 bg-black text-white py-2 rounded-lg"
            )

            # Link to login
            ui.label("Already have an account?").classes("mt-4 text-gray-600")
            ui.link("Sign In", "/login").classes("text-black hover:underline")
