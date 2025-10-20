from nicegui import ui, app
from sidebar import show_sidebar

# --- Mock Data (for demonstration purposes) ---
# In a real application, this data would come from a database.
REPORTS_DATA = [
    {
        "id": "#5821",
        "category": "Pothole",
        "location": "Osu, Accra",
        "submitted_by": "user@example.com",
        "submitted_on": "2024-07-22",
        "status": "Pending",
        "details": "A large pothole is causing traffic issues.",
    },
    {
        "id": "#5820",
        "category": "Sanitation",
        "location": "East Legon, Accra",
        "submitted_by": "another_user@example.com",
        "submitted_on": "2024-07-21",
        "status": "In Progress",
        "details": "Waste has not been collected for over a week.",
    },
    {
        "id": "#5819",
        "category": "Broken Light",
        "location": "Madina, Accra",
        "submitted_by": "user@example.com",
        "submitted_on": "2024-07-20",
        "status": "Resolved",
        "details": "Streetlight on the main road is broken.",
    },
]


def show_admin_dashboard():
    """Creates the UI for the admin dashboard with full controls."""
    show_sidebar()

    with ui.column().classes("w-full h-full p-8 bg-gray-50 overflow-auto"):
        ui.label("Admin Dashboard Overview").classes(
            "text-4xl font-bold text-gray-800 mb-8"
        )
        # The rest of the admin dashboard UI (KPIs, charts) would go here.
        # For brevity, we'll link directly to the full-featured reports page.
        ui.label(
            "Welcome, Admin. You have full access to manage all reports and users."
        ).classes("text-lg mb-4")
        ui.button(
            "Manage All Reports", on_click=lambda: ui.navigate.to("/admin/reports")
        ).props("color=black")


def show_authority_dashboard():
    """Creates the UI for an authority to view and update reports."""
    show_sidebar()

    with ui.column().classes("w-full p-8"):
        ui.label("Assigned Reports").classes("text-3xl font-bold mb-6")

        async def update_status_dialog(report: dict):
            with ui.dialog() as dialog, ui.card():
                ui.label(f"Update Status for {report['id']}").classes(
                    "text-lg font-bold"
                )
                ui.label(f"Category: {report['category']}")
                ui.label(f"Location: {report['location']}")
                status_select = ui.select(
                    ["Pending", "In Progress", "Resolved", "Rejected"],
                    label="New Status",
                    value=report["status"],
                ).classes("w-full")
                with ui.row().classes("w-full justify-end"):
                    ui.button("Cancel", on_click=dialog.close)
                    ui.button(
                        "Update",
                        on_click=lambda: (
                            ui.notify(
                                f"Status for {report['id']} updated to {status_select.value}"
                            ),
                            dialog.close(),
                        ),
                    )
            await dialog

        for report in REPORTS_DATA:
            with ui.card().classes("w-full"):
                with ui.row().classes("w-full items-center justify-between"):
                    with ui.column():
                        ui.label(report["category"]).classes("text-lg font-bold")
                        ui.label(f"{report['id']} - {report['location']}").classes(
                            "text-gray-600"
                        )
                    with ui.row().classes("items-center gap-2"):
                        ui.badge(
                            report["status"],
                            color={
                                "Pending": "orange",
                                "In Progress": "blue",
                                "Resolved": "green",
                            }.get(report["status"], "grey"),
                        )
                        ui.button(
                            "Update Status",
                            on_click=lambda r=report: update_status_dialog(r),
                        ).props("flat")


def show_user_dashboard():
    """Creates the UI for a regular user to view their reports."""
    show_sidebar()

    with ui.column().classes("w-full p-8"):
        ui.label("My Submitted Reports").classes("text-3xl font-bold mb-6")

        # In a real app, you'd filter reports for the logged-in user.
        # e.g., reports = db.get_reports(user_id=app.storage.user['id'])
        user_reports = [
            r for r in REPORTS_DATA if r["submitted_by"] == "user@example.com"
        ]

        if not user_reports:
            ui.label("You haven't submitted any reports yet.").classes("text-gray-500")
            return

        for report in user_reports:
            with ui.card().classes("w-full"):
                with ui.row().classes("w-full items-center justify-between"):
                    with ui.column():
                        ui.label(report["category"]).classes("text-lg font-bold")
                        ui.label(f"{report['id']} - {report['location']}").classes(
                            "text-gray-600"
                        )
                    ui.badge(
                        report["status"],
                        color={
                            "Pending": "orange",
                            "In Progress": "blue",
                            "Resolved": "green",
                        }.get(report["status"], "grey"),
                    ).classes("p-2")


@ui.page("/dashboard")
def show_dashboard():
    """
    This function acts as a router, displaying the correct dashboard
    based on the user's role stored in the session.
    """
    # In a real app, you would get the role after the user logs in.
    # We'll use a query parameter for demonstration: /dashboard?role=admin
    # A better way is to set it in app.storage.user after login.
    # For example, in your login logic: app.storage.user['role'] = 'admin'
    role = app.storage.user.get("role")

    if not role:
        # If no role is found, redirect to login. This protects the page.
        ui.navigate.to("/login")
        ui.label("Redirecting to login...")
        return

    # Render the dashboard based on the role
    if role == "admin":  # Match lowercase role from backend
        show_admin_dashboard()
    elif role == "authority":  # Match lowercase role from backend
        show_authority_dashboard()
    elif role == "user":  # Match lowercase role from backend
        show_user_dashboard()
    else:
        # Fallback for unknown roles
        ui.label(f"Unknown role: {role}")
        ui.button("Back to Home", on_click=lambda: ui.navigate.to("/"))


@ui.page("/login_simulation/{role}")
def login_simulation(role: str):
    """A helper page to simulate logging in and setting a role."""
    # In a real login page, you would set this after verifying credentials.
    app.storage.user["role"] = role
    ui.notify(f"Simulating login as: {role}", type="positive")
    ui.navigate.to("/dashboard")
