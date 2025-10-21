from nicegui import ui, app


from home import *
from dashboard import *
from auth.update_report import *
from auth.reports import *
from auth.analytics import *
from user.submit_report import *
from user.view_report import *
from login import *
from signup import *


#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")


@ui.page("/")
def main_page():

    # Import Font Awesome
    ui.add_head_html(
        '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">'
    )

    show_home()


ui.run(storage_secret="tgdsgdyudjjsijd")
