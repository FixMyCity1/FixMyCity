from nicegui import ui, app, run
import requests
import mimetypes
from sidebar import show_sidebar
from utils.api import base_url


@ui.page("/user/submit_report")
def submit_report():
    show_sidebar()

    ui.label("Report a City Issue").classes("text-4xl font-bold text-gray-800 mb-2")
    ui.label("Help us improve our community by reporting problems.").classes(
        "text-gray-600 mb-10"
    )

    # Input fields
    category = (
        ui.select(
            [
                "Potholes",
                "Waste Management",
                "Water Supply",
                "Electricity Outage",
                "Roads & Traffic",
                "Public Safety",
                "Illegal Construction",
                "Environmental Pollution",
                "Other",
            ],
            label="Select a category",
        )
        .props("outlined dense")
        .classes("w-full max-w-xl")
    )

    title = (
        ui.input("e.g., Large pothole on Main St")
        .props("outlined dense")
        .classes("w-full max-w-xl")
    )
    description = (
        ui.textarea("Describe the issue in detail...")
        .props("outlined dense")
        .classes("w-full max-w-xl")
    )
    region = (
        ui.input("e.g., Osu, Accra").props("outlined dense").classes("w-full max-w-xl")
    )
    gps_address = (
        ui.input("e.g., GA-435-0123 or Google Maps link")
        .props("outlined dense")
        .classes("w-full max-w-xl")
    )

    # Dictionary to store uploaded file data
    uploaded_file_data = {}

    def handle_file_upload(e):
        """Handles the file upload event, storing content, name, and MIME type."""
        try:
            # e.content is bytes directly in NiceGUI upload event
            uploaded_file_data["content"] = e.content
            uploaded_file_data["name"] = e.name
            # Detect MIME type from file extension
            mime_type, _ = mimetypes.guess_type(e.name)
            uploaded_file_data["mime_type"] = mime_type or "application/octet-stream"
            ui.notify(f"File '{e.name}' ready for submission.", type="positive")
        except Exception as ex:
            ui.notify(f"Error processing file: {ex}", type="negative")
            uploaded_file_data.clear()  # Clear any partial data if reading fails

    flyer_upload = (
        ui.upload(
            label="Upload a file (PNG, JPG, GIF up to 10MB)",
            multiple=False,
            max_file_size=10_000_000,
        )
        .props("flat bordered color=black")
        .on_upload(handle_file_upload)  # Assign the handler here
        .classes("w-full max-w-xl")
    )

    status_label = ui.label("").classes("text-red-500 mt-3 hidden")
    spinner = ui.spinner(size="lg").classes("hidden text-black")

    # --- Submit Handler ---
    async def handle_submit():
        if not all(
            [
                category.value,
                title.value,
                description.value,
                region.value,
                gps_address.value,
            ]
        ):
            status_label.text = "Please fill in all required fields."
            status_label.classes(remove="hidden")
            return

        if not uploaded_file_data.get("content"):  # Check if content was stored
            status_label.text = "Please upload an image flyer."
            status_label.classes(remove="hidden")
            return

        status_label.classes(add="hidden")
        spinner.classes(remove="hidden")

        flyer_content = uploaded_file_data["content"]
        flyer_name = uploaded_file_data["name"]

        def send_request():
            try:
                token = app.storage.user.get(
                    "access_token"
                )  # Assuming JWT or token stored on login
                headers = {"Authorization": f"Bearer {token}"} if token else {}

                # Use the stored file name, content, and MIME type
                mime_type = uploaded_file_data.get(
                    "mime_type", "application/octet-stream"
                )
                files = {"flyer": (flyer_name, flyer_content, mime_type)}
                data = {
                    "title": title.value,
                    "description": description.value,
                    "region": region.value,
                    "gps_location": gps_address.value,
                    "category": category.value,
                }

                return requests.post(
                    f"{base_url}/issues", data=data, files=files, headers=headers
                )
            except requests.exceptions.RequestException as e:
                return e

        response = await run.io_bound(send_request)
        spinner.classes(add="hidden")

        # Handle backend responses
        if isinstance(response, requests.exceptions.RequestException):
            status_label.text = f"Connection error: {response}"
            status_label.classes(remove="hidden")
            return

        if response.status_code == 200:
            ui.notify("Issue reported successfully!", type="positive")
            # Optionally reset form
            title.value = ""
            description.value = ""
            region.value = ""
            gps_address.value = ""
            category.value = None
            uploaded_file_data.clear()  # Clear the stored data
        elif response.status_code == 409:
            ui.notify("An issue with this title already exists.", type="warning")
        elif response.status_code == 401:
            ui.notify("Please login again. Session expired.", type="warning")
            ui.navigate.to("/login")
        else:
            status_label.text = f"Error: {response.text}"
            status_label.classes(remove="hidden")

    ui.button("Submit Report", on_click=handle_submit).classes(
        "w-full max-w-xl py-3 mt-6 text-white bg-black rounded-lg"
    )
