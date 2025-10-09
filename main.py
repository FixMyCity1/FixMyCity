from nicegui import ui, app
from pages import (
    add_advert,
    adverts,
    dashboard,
    edit_advert,
    login,
    view_advert,
    home,
    signup,
)
from components import sidebar, footer, header

#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")


home.show_home()
add_advert.show_add_advert()
adverts.show_adverts()
dashboard.show_dashboard()
edit_advert.show_edit_advert()
login.show_login()
view_advert.show_view_advert()
signup.show_signup()
sidebar.show_sidebar()
footer.show_footer()

ui.run()
