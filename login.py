from nicegui import ui, app, run
import requests
from utils.api import base_url


@ui.page("/login")
def show_login():
    ui.query(".nicegui-content").classes("m-0 p-0")

    with ui.row().classes("w-full h-screen m-0 p-0 gap-0"):
        # Left side login form
        with ui.column().classes(
            "w-2/5 h-full justify-center items-center bg-white p-10"
        ):
            ui.label("Login").classes("text-3xl font-bold mb-6")

            email = ui.input("Email").classes("w-80 mb-4")
            password = ui.input(
                "Password", password=True, password_toggle_button=True
            ).classes("w-80 mb-6")

            spinner = ui.spinner(size="lg").classes("hidden text-black")
            result_label = ui.label("").classes("text-red-500 mt-4")

            async def handle_login():
                """Handle login by sending credentials to the backend API."""
                if not email.value or not password.value:
                    result_label.text = "Please fill in all fields."
                    result_label.classes(remove="hidden")
                    return

                spinner.classes(remove="hidden")
                result_label.classes(add="hidden")

                def send_request() -> (
                    requests.Response | requests.exceptions.RequestException
                ):
                    """Send login request to backend."""
                    try:
                        # The backend expects 'email' and form-urlencoded data.
                        return requests.post(
                            f"{base_url}/users/login",
                            data={"email": email.value, "password": password.value},
                            headers={
                                "Content-Type": "application/x-www-form-urlencoded"
                            },
                        )
                    except requests.exceptions.RequestException as e:
                        return e

                response = await run.io_bound(send_request)
                spinner.classes(add="hidden")

                if isinstance(response, requests.exceptions.RequestException):
                    result_label.text = f"Connection error: {response}"
                    result_label.classes(remove="hidden")
                    return

                if response.status_code == 200:
                    user_data = response.json()
                    app.storage.user.update(user_data)
                    ui.notify("Login successful!", type="positive")
                    ui.navigate.to("/dashboard")
                elif response.status_code in [400, 401]:
                    result_label.text = "Invalid email or password."
                    result_label.classes(remove="hidden")
                else:
                    result_label.text = f"An unexpected error occurred: {response.text}"
                    result_label.classes(remove="hidden")

            ui.button("Sign In", on_click=handle_login).classes(
                "w-80 bg-black text-white py-2 rounded-lg"
            )

            with ui.row().classes("mt-4 items-center"):
                ui.label("Don't have an account?").classes("text-gray-600")
                ui.link("Sign up here", "/signup").classes(
                    "text-black hover:underline ml-1"
                )

            ui.separator().classes("w-80 my-4")

            ui.button(
                "Back to Home",
                on_click=lambda: ui.navigate.to("/"),
            ).props(
                "flat color=black"
            ).classes("w-80")

        # Right side image
        with ui.element("div").classes("w-3/5 h-full relative"):
            ui.image("/assets/login2.jpg").classes(
                "w-full h-full object-cover rounded-lg shadow-lg"
            )
            with ui.column().classes(
                "absolute inset-0 bg-black/40 flex justify-end p-12 text-white"
            ):
                ui.label("FixMyCity").classes("text-5xl font-bold")
                ui.label(
                    "Your voice for a better community. Report issues, see results."
                ).classes("text-2xl text-gray-200 mt-2")
