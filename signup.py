from nicegui import ui, run
import requests
import asyncio
from utils.api import base_url


@ui.page("/signup")
def show_signup():
    """Displays the signup page and handles user registration."""
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
            username = ui.input("Username").classes("w-80 mb-4")
            email = ui.input("Email").classes("w-80 mb-4")
            password = ui.input(
                "Password", password=True, password_toggle_button=True
            ).classes("w-80 mb-4")
            confirm_password = ui.input(
                "Confirm Password", password=True, password_toggle_button=True
            ).classes("w-80 mb-4")

            # Role selection
            role = ui.select(
                ["User", "Authority"],
                label="Select Role",
                value="User",
            ).classes("w-80 mb-6")

            # Loading indicator
            spinner = ui.spinner(size="lg").classes("hidden text-black")

            async def handle_signup():
                """Handle signup process by sending data to the backend API."""
                if not all(
                    [
                        username.value,
                        email.value,
                        password.value,
                        confirm_password.value,
                    ]
                ):
                    ui.notify("Please fill in all fields.", type="warning")
                    return

                if password.value != confirm_password.value:
                    ui.notify("Passwords do not match.", type="negative")
                    return

                # ✅ Map frontend role to backend-accepted values
                backend_role = "authorities" if role.value == "Authority" else "user"

                payload = {
                    "username": username.value,
                    "email": email.value,
                    "password": password.value,
                    "role": backend_role,
                }

                spinner.classes(remove="hidden")  # show spinner

                def send_request():
                    """Send signup request to backend."""
                    try:
                        return requests.post(f"{base_url}/users/register", data=payload)
                    except requests.exceptions.RequestException as e:
                        return e

                result = await run.io_bound(send_request)
                spinner.classes(add="hidden")  # hide spinner

                if isinstance(result, requests.exceptions.RequestException):
                    ui.notify(
                        f"Could not connect to the server: {result}", type="negative"
                    )
                    return

                # ✅ Handle backend responses
                if result.status_code == 200:
                    ui.notify("Signup successful! Please log in.", type="positive")
                    await asyncio.sleep(2)  # Wait for 2 seconds before redirecting
                    ui.navigate.to("/login")
                elif result.status_code == 409:
                    ui.notify(
                        "A user with this email or username already exists.",
                        type="warning",
                    )
                elif result.status_code == 422:
                    ui.notify(
                        "Invalid input. Please check your details.", type="warning"
                    )
                elif result.status_code >= 500:
                    ui.notify("Server error. Please try again later.", type="negative")
                else:
                    try:
                        message = result.json().get("detail", result.text)
                    except Exception:
                        message = result.text
                    ui.notify(
                        f"An unexpected error occurred: {message}", type="negative"
                    )

            # Signup button
            ui.button("Sign Up", on_click=handle_signup).classes(
                "w-80 bg-black text-white py-2 rounded-lg mt-4"
            )

            # Link to login
            ui.label("Already have an account?").classes("mt-4 text-gray-600")
            ui.link("Sign In", "/login").classes("text-black hover:underline")
