from nicegui import ui, app
from components.header import show_header
from components.footer import show_footer


@ui.page("/")
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

    with ui.column().classes("w-full items-center bg-white py-20 px-4"):
        # Welcome Section
        with ui.column().classes("w-full max-w-6xl mx-auto items-center mb-16"):
            # Main Title
            ui.label("Welcome to FixMyCity").classes(
                "text-5xl text-black font-bold tracking-tight text-center mb-12"
            )

            # Two-column layout for image and text
            with ui.row().classes("w-full items-center m-0 p-0 gap-0"):
                ui.image(
                    "https://placehold.co/800x600/e0e0e0/333?text=FixMyCity"
                ).classes("rounded-lg w-1/2 shadow-xl")

                # Right side: Text
                with ui.column().classes("w-1/2 justify-center items-center p-10"):
                    ui.label(
                        "FixMyCity is a platform that allows citizens to report civic issues in their communities — such as sanitation problems, potholes, broken infrastructure, public safety concerns, or illegal drug havens. Your reports are forwarded to the appropriate authorities for quick action, helping create cleaner, safer, and more sustainable cities in Ghana."
                    ).classes("text-xl text-gray-600 leading-relaxed")

        # Services Section
        ui.label("HOW IT WORKS").classes(
            "text-lg text-gray-500 font-serif tracking-widest"
        )
        ui.label("A Simple Process for Change").classes(
            "text-4xl text-black font-bold mb-8"
        )

        # Service Cards
        with ui.row().classes("w-full justify-center gap-8"):
            # Card 1
            with ui.card().classes(
                "w-72 h-96 flex flex-col justify-end p-6 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('https://placehold.co/600x400/1f2937/white?text=Report'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("Report an Issue").classes("text-2xl font-bold")
                    ui.label(
                        "Quickly submit a report with photos and location."
                    ).classes("text-gray-300")

            # Card 2
            with ui.card().classes(
                "w-72 h-96 flex flex-col justify-end p-6 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('https://placehold.co/600x400/1f2937/white?text=Investigate'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("We Investigate").classes("text-2xl font-bold")
                    ui.label(
                        "Your report is forwarded to the right authority or NGO."
                    ).classes("text-gray-300")

            # Card 3
            with ui.card().classes(
                "w-72 h-96 flex flex-col justify-end p-6 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('https://placehold.co/600x400/1f2937/white?text=Fixed'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("Get it Fixed").classes("text-2xl font-bold")
                    ui.label("Receive updates and see the issue get resolved.").classes(
                        "text-gray-300"
                    )

        # Testimonials Section
        with ui.column().classes("w-full items-center pt-20 pb-24 px-4 bg-white"):
            ui.label("TESTIMONIALS").classes(
                "text-lg text-gray-500 font-serif tracking-widest"
            )
            ui.label("What Our Citizens Say").classes(
                "text-4xl text-black font-bold mb-12 text-center"
            )

            with ui.row().classes(
                "w-full max-w-7xl justify-center gap-8 items-stretch flex-wrap"
            ):
                # Testimonial 1
                with ui.card().classes(
                    "w-full md:w-2/5 flex flex-col items-center text-center p-8 shadow-lg"
                ):
                    ui.image(
                        "https://placehold.co/100x100/e0e0e0/333?text=User"
                    ).classes("w-24 h-24 rounded-full mb-4")
                    ui.label(
                        '"I reported a huge pothole on my street, and it was fixed within a week! FixMyCity actually works."'
                    ).classes("flex-grow text-lg italic text-gray-600 mb-4")
                    ui.label("Ama Serwaa").classes("font-bold text-lg")
                    ui.label("Resident, Osu").classes("text-gray-500")

                # Testimonial 2
                with ui.card().classes(
                    "w-full md:w-2/5 flex flex-col items-center text-center p-8 shadow-lg"
                ):
                    ui.image(
                        "https://placehold.co/100x100/e0e0e0/333?text=User"
                    ).classes("w-24 h-24 rounded-full mb-4")
                    ui.label(
                        '"A broken water pipe in our area was causing a lot of waste. I reported it on FixMyCity, and Ghana Water Company was notified and fixed it in two days. Incredible service!"'
                    ).classes("flex-grow text-lg italic text-gray-600 mb-4")
                    ui.label("Nii Armah").classes("font-bold text-lg")
                    ui.label("Resident, East Legon").classes("text-gray-500")

                # Testimonial 3
                with ui.card().classes(
                    "w-full md:w-2/5 flex flex-col items-center text-center p-8 shadow-lg"
                ):
                    ui.image(
                        "https://placehold.co/100x100/e0e0e0/333?text=User"
                    ).classes("w-24 h-24 rounded-full mb-4")
                    ui.label(
                        '"Illegal dumping near the market was a huge health hazard. After multiple reports on the platform, the local assembly organized a cleanup. The area is so much better now."'
                    ).classes("flex-grow text-lg italic text-gray-600 mb-4")
                    ui.label("Adwoa Boateng").classes("font-bold text-lg")
                    ui.label("Shop Owner, Madina").classes("text-gray-500")

                # Testimonial 4
                with ui.card().classes(
                    "w-full md:w-2/5 flex flex-col items-center text-center p-8 shadow-lg"
                ):
                    ui.image(
                        "https://placehold.co/100x100/e0e0e0/333?text=User"
                    ).classes("w-24 h-24 rounded-full mb-4")
                    ui.label(
                        "\"The streetlights on my campus road were out for weeks, making it unsafe at night. I reported it, and now they're all working. It's great to see a platform that gets results.\""
                    ).classes("flex-grow text-lg italic text-gray-600 mb-4")
                    ui.label("Ben Quarshie").classes("font-bold text-lg")
                    ui.label("Student, Dansoman").classes("text-gray-500")

                # Testimonial 5
                with ui.card().classes(
                    "w-full md:w-2/5 flex flex-col items-center text-center p-8 shadow-lg"
                ):
                    ui.image(
                        "https://placehold.co/100x100/e0e0e0/333?text=User"
                    ).classes("w-24 h-24 rounded-full mb-4")
                    ui.label(
                        '"A spot in our neighborhood became a haven for drug abuse, making us feel unsafe. We reported it on FixMyCity, and the police increased patrols, clearing the area. It\'s a relief for the community."'
                    ).classes("flex-grow text-lg italic text-gray-600 mb-4")
                    ui.label("Kofi Mensah").classes("font-bold text-lg")
                    ui.label("Resident, Nima").classes("text-gray-500")

        # Blog and Articles Section
        with ui.column().classes(
            "w-full items-center pt-20 pb-24 px-4 bg-gray-50 mt-16"
        ):
            ui.label("FROM OUR BLOG").classes(
                "text-lg text-gray-500 font-serif tracking-widest"
            )
            ui.label("Updates & Success Stories").classes(
                "text-4xl text-black font-bold mb-12 text-center"
            )

            with ui.row().classes("w-full justify-center items-stretch gap-8"):
                # Blog Post 1
                with ui.card().classes("w-96"):
                    ui.image("/assets/blog1.jpg")
                    with ui.card_section():
                        ui.label("Community Cleanup a Huge Success in Madina").classes(
                            "text-xl font-bold my-2"
                        )
                        ui.label(
                            "Read about how residents came together to transform their neighborhood..."
                        ).classes("text-gray-600 mb-4")
                        ui.button("Read More").props("flat color=black")

                # Blog Post 2
                with ui.card().classes("w-96"):
                    ui.image("/assets/blog2.jpg")
                    with ui.card_section():
                        ui.label(
                            "Pothole Patrol: How Your Reports Are Fixing Roads"
                        ).classes("text-xl font-bold my-2")
                        ui.label(
                            "A look into the data and the impact of citizen reporting on infrastructure..."
                        ).classes("text-gray-600 mb-4")
                        ui.button("Read More").props("flat color=black")

                # Blog Post 3
                with ui.card().classes("w-96"):
                    ui.image("/assets/blog3.jpg")
                    with ui.card_section():
                        ui.label("New Partnership with the EPA Announced").classes(
                            "text-xl font-bold my-2"
                        )
                        ui.label(
                            "We're excited to work with the Environmental Protection Agency to tackle sanitation..."
                        ).classes("text-gray-600 mb-4")
                        ui.button("Read More").props("flat color=black")

        # Upcoming Events Section
        with ui.column().classes("w-full items-center pt-20 pb-24 px-4 bg-white"):
            ui.label("COMMUNITY ACTION").classes(
                "text-lg text-gray-500 font-serif tracking-widest"
            )
            ui.label("Upcoming Initiatives").classes(
                "text-4xl text-black font-bold mb-12 text-center"
            )

            with ui.column().classes("w-full max-w-4xl gap-6"):
                # Event 1
                with ui.row().classes(
                    "w-full items-center p-6 border rounded-xl shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-4 rounded-lg mr-6"
                    ):
                        ui.label("JUL").classes("text-lg font-bold text-black")
                        ui.label("25").classes("text-4xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Osu Community Cleanup Day").classes(
                            "text-2xl font-bold"
                        )
                        ui.label("Oxford Street, Osu, Accra").classes("text-gray-600")
                    ui.button("Volunteer").props("color=black")

                # Event 2
                with ui.row().classes(
                    "w-full items-center p-6 border rounded-xl shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-4 rounded-lg mr-6"
                    ):
                        ui.label("AUG").classes("text-lg font-bold text-black")
                        ui.label("15").classes("text-4xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Town Hall Meeting on Public Safety").classes(
                            "text-2xl font-bold"
                        )
                        ui.label("Online via Zoom").classes("text-gray-600")
                    ui.button("Join Meeting").props("color=black")

                # Event 3
                with ui.row().classes(
                    "w-full items-center p-6 border rounded-xl shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-4 rounded-lg mr-6"
                    ):
                        ui.label("SEP").classes("text-lg font-bold text-black")
                        ui.label("05").classes("text-4xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Neighborhood Watch Training").classes(
                            "text-2xl font-bold"
                        )
                        ui.label("East Legon Police Station").classes("text-gray-600")
                    ui.button("Register").props("color=black")

        # Customer Service Centers Section
        with ui.column().classes("w-full items-center pt-20 pb-24 px-4 bg-gray-50"):
            ui.label("OUR PARTNERS").classes(
                "text-lg text-gray-500 font-serif tracking-widest"
            )
            ui.label("Working With Government Authorities").classes(
                "text-4xl text-black font-bold mb-12 text-center"
            )

            with ui.row().classes("w-full max-w-5xl justify-center gap-x-16 gap-y-8"):
                # Column for Government Authorities
                with ui.column().classes("gap-4 items-center"):
                    for authority in [
                        "Environmental Protection Agency (EPA)",
                        "Ghana Police Service",
                        "Ghana National Fire Service",
                        "National Disaster Management Org. (NADMO)",
                        "Metropolitan & Municipal Assemblies (MMDAs)",
                        "Narcotics Control Commission",
                        "Department of Urban Roads",
                    ]:
                        ui.label(authority).classes("text-lg text-gray-600")

    show_footer()
