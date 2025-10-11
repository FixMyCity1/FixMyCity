from nicegui import ui, app

from user import add_report, view_report
from components import footer
from components import header
from authority import sidebar, reports, dashboard
import home


#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Import Font Awesome
ui.add_head_html(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">'
)

# Import Google Fonts
ui.add_head_html(
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">'
)

header.show_header()
home.show_home()
add_report.show_add_report()
view_report.show_view_report()
reports.show_reports()
dashboard.show_dashboard()
sidebar.show_sidebar()
footer.show_footer()

ui.run()
