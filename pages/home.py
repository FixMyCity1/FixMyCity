from nicegui import ui, app
from components.header import show_header


def show_home():
    ui.query(".nicegui-content").classes("m-0 p-0")
    show_header()

    with ui.element("div").classes("relative w-full h-screen"):

        # Background carousel
        with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-screen h-screen z-[-2]"
        ).style("width: 100vw; height: 100vh;"):
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home1.png); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home2.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home3.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home4.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home5.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home6.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home7.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
            with ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home8.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                pass
