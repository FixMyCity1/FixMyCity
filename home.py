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
            with ui.carousel_slide().classes("w-screen h-screen relative").style(
                "background-image: url(/assets/caro2.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                with ui.element("div").classes(
                    "absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-center p-4"
                ):
                    ui.label("See an Issue? Report It!").classes(
                        "text-4xl md:text-5xl font-extrabold text-white mb-3 drop-shadow-lg"
                    )
                    ui.label("Your voice helps build a better city.").classes(
                        "text-lg md:text-xl text-gray-200 max-w-xl"
                    )

            with ui.carousel_slide().classes("w-screen h-screen relative").style(
                "background-image: url(/assets/caro3.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                with ui.element("div").classes(
                    "absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-center p-4"
                ):
                    ui.label("Together, We Fix Our City").classes(
                        "text-4xl md:text-5xl font-extrabold text-white mb-3 drop-shadow-lg"
                    )
                    ui.label("Join a community dedicated to positive change.").classes(
                        "text-lg md:text-xl text-gray-200 max-w-xl"
                    )

            with ui.carousel_slide().classes("w-screen h-screen relative").style(
                "background-image: url(/assets/caro4.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                with ui.element("div").classes(
                    "absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-center p-4"
                ):
                    ui.label("Swift Action, Real Results").classes(
                        "text-4xl md:text-5xl font-extrabold text-white mb-3 drop-shadow-lg"
                    )
                    ui.label(
                        "We connect your reports to the right authorities."
                    ).classes("text-lg md:text-xl text-gray-200 max-w-xl")

            with ui.carousel_slide().classes("w-screen h-screen relative").style(
                "background-image: url(/assets/caro6.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                with ui.element("div").classes(
                    "absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-center p-4"
                ):
                    ui.label("Make a Difference Today").classes(
                        "text-4xl md:text-5xl font-extrabold text-white mb-3 drop-shadow-lg"
                    )
                    ui.label(
                        "Every report contributes to a cleaner, safer Ghana."
                    ).classes("text-lg md:text-xl text-gray-200 max-w-xl")

            with ui.carousel_slide().classes("w-screen h-screen relative").style(
                "background-image: url(/assets/caro5.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            ):
                with ui.element("div").classes(
                    "absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-center p-4"
                ):
                    ui.label("Empowering Citizens, Improving Cities").classes(
                        "text-4xl md:text-5xl font-extrabold text-white mb-3 drop-shadow-lg"
                    )
                    ui.label("Your platform for civic engagement.").classes(
                        "text-lg md:text-xl text-gray-200 max-w-xl"
                    )

    with ui.column().classes("w-full items-center bg-white py-16 px-4"):
        # Welcome Section
        with ui.column().classes(
            "w-full max-w-5xl mx-auto items-center mb-12 scroll-animate-section"
        ):
            # Main Title
            ui.label("Welcome to FixMyCity").classes(
                "text-4xl text-black font-bold tracking-tight text-center mb-8"
            )

            # Two-column layout for image and text
            with ui.row().classes(
                "w-full items-center m-0 p-0 gap-0"
            ):  # This row itself doesn't need animation, its parent column does.
                ui.image("/assets/caro1.jpg").classes("rounded-lg w-1/2 shadow-lg")

                # Right side: Text
                with ui.column().classes("w-1/2 justify-center items-center p-8"):
                    ui.label(
                        "FixMyCity is a platform that allows citizens to report civic issues in their communities — such as sanitation problems, potholes, broken infrastructure, public safety concerns, or illegal drug havens. Your reports are forwarded to the appropriate authorities for quick action, helping create cleaner, safer, and more sustainable cities in Ghana."
                    ).classes("text-lg text-gray-600 leading-relaxed")

        # Services Section
        ui.label("HOW IT WORKS").classes(
            "text-base text-gray-500 font-serif tracking-widest"
        )
        ui.label("A Simple Process for Change").classes(
            "text-3xl text-black font-bold mb-6"
        )

        # Service Cards
        with ui.row().classes("w-full justify-center gap-6"):
            # Card 1
            with ui.card().classes(
                "w-64 h-80 flex flex-col justify-end p-4 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('/assets/report.jpg'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("Report an Issue").classes("text-xl font-bold")
                    ui.label(
                        "Quickly submit a report with photos and location."
                    ).classes("text-sm text-gray-300")

            # Card 2
            with ui.card().classes(
                "w-64 h-80 flex flex-col justify-end p-4 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('/assets/invest.jpg'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("We Investigate").classes("text-xl font-bold")
                    ui.label(
                        "Your report is forwarded to the right authority or NGO."
                    ).classes("text-sm text-gray-300")

            # Card 3
            with ui.card().classes(
                "w-64 h-80 flex flex-col justify-end p-4 text-white relative group overflow-hidden"
            ).style(
                "background-image: url('/assets/fix.jpg'); background-size: cover; background-position: center;"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                )
                with ui.element("div").classes("relative"):
                    ui.label("Get it Fixed").classes("text-xl font-bold")
                    ui.label("Receive updates and see the issue get resolved.").classes(
                        "text-sm text-gray-300"
                    )
        # Testimonials Section
        with ui.column().classes(
            "w-full items-center pt-16 pb-20 px-4 bg-white scroll-animate-section"
        ):
            ui.label("TESTIMONIALS").classes(
                "text-base text-gray-500 font-serif tracking-widest"
            )
            ui.label("What Our Citizens Say").classes(
                "text-3xl text-black font-bold mb-8 text-center"
            )

            with ui.row().classes(
                "w-full max-w-6xl justify-center gap-6 items-stretch flex-wrap"
            ):
                # Testimonial 1
                with ui.card().classes(
                    "w-64 h-80 flex flex-col justify-end p-4 text-white relative overflow-hidden"
                ).style(
                    "background-image: url('/assets/ama.jpg'); background-size: cover; background-position: center;"
                ):
                    ui.element("div").classes(
                        "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                    )
                    with ui.element("div").classes("relative"):
                        ui.label(
                            '"I reported a huge pothole on my street, and it was fixed within a week! FixMyCity actually works."'
                        ).classes("text-base italic text-gray-200 mb-2")
                        ui.label("— Ama Serwaa").classes("font-bold text-base")
                        ui.label("Resident, Osu").classes("text-sm text-gray-300")

                # Testimonial 2
                with ui.card().classes(
                    "w-64 h-80 flex flex-col justify-end p-4 text-white relative overflow-hidden"
                ).style(
                    "background-image: url('/assets/nii.jpg'); background-size: cover; background-position: center;"
                ):
                    ui.element("div").classes(
                        "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                    )
                    with ui.element("div").classes("relative"):
                        ui.label(
                            '"A broken water pipe in our area was causing a lot of waste. I reported it on FixMyCity, and Ghana Water Company was notified and fixed it in two days. Incredible service!"'
                        ).classes("text-base italic text-gray-200 mb-2")
                        ui.label("— Nii Armah").classes("font-bold text-base")
                        ui.label("Resident, East Legon").classes(
                            "text-sm text-gray-300"
                        )

                # Testimonial 3
                with ui.card().classes(
                    "w-64 h-80 flex flex-col justify-end p-4 text-white relative overflow-hidden"
                ).style(
                    "background-image: url('/assets/adwoa.jpg'); background-size: cover; background-position: center;"
                ):
                    ui.element("div").classes(
                        "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                    )
                    with ui.element("div").classes("relative"):
                        ui.label(
                            '"Illegal dumping near the market was a huge health hazard. After multiple reports on the platform, the local assembly organized a cleanup. The area is so much better now."'
                        ).classes("text-base italic text-gray-200 mb-2")
                        ui.label("— Adwoa Boateng").classes("font-bold text-base")
                        ui.label("Shop Owner, Madina").classes("text-sm text-gray-300")

                # Testimonial 4
                with ui.card().classes(
                    "w-64 h-80 flex flex-col justify-end p-4 text-white relative overflow-hidden"
                ).style(
                    "background-image: url('/assets/ben.jpg'); background-size: cover; background-position: center;"
                ):
                    ui.element("div").classes(
                        "absolute inset-0 bg-gradient-to-t from-black via-black/70 to-transparent"
                    )
                    with ui.element("div").classes("relative"):
                        ui.label(
                            "\"The streetlights on my campus road were out for weeks, making it unsafe at night. I reported it, and now they're all working. It's great to see a platform that gets results.\""
                        ).classes("text-base italic text-gray-200 mb-2")
                        ui.label("— Ben Quarshie").classes("font-bold text-base")
                        ui.label("Student, Dansoman").classes("text-sm text-gray-300")

        # Blog and Articles Section
        with ui.column().classes(
            "scroll-animate-section "
            + "w-full items-center pt-16 pb-20 px-4 bg-gray-50 mt-12"
        ):
            ui.label("FROM OUR BLOG").classes(
                "text-base text-gray-500 font-serif tracking-widest"
            )
            ui.label("Updates & Success Stories").classes(
                "text-3xl text-black font-bold mb-8 text-center"
            )

            with ui.row().classes("w-full justify-center items-stretch gap-6"):
                # Blog Post 1
                with ui.card().classes("w-80"):
                    ui.image("/assets/blog1.jpg")
                    with ui.card_section():
                        ui.label("Community Cleanup a Huge Success in Madina").classes(
                            "text-lg font-bold my-1"
                        )
                        ui.label(
                            "Read about how residents came together to transform their neighborhood..."
                        ).classes("text-sm text-gray-600 mb-2")
                        ui.button("Read More").props("flat color=black")

                # Blog Post 2
                with ui.card().classes("w-80"):
                    ui.image("/assets/blog2.jpg")
                    with ui.card_section():
                        ui.label(
                            "Pothole Patrol: How Your Reports Are Fixing Roads"
                        ).classes("text-lg font-bold my-1")
                        ui.label(
                            "A look into the data and the impact of citizen reporting on infrastructure..."
                        ).classes("text-sm text-gray-600 mb-2")
                        ui.button("Read More").props("flat color=black")

                # Blog Post 3
                with ui.card().classes("w-80"):
                    ui.image("/assets/blog3.jpg")
                    with ui.card_section():
                        ui.label("New Partnership with the EPA Announced").classes(
                            "text-lg font-bold my-1"
                        )
                        ui.label(
                            "We're excited to work with the Environmental Protection Agency to tackle sanitation..."
                        ).classes("text-sm text-gray-600 mb-2")
                        ui.button("Read More").props("flat color=black")

        # Upcoming Events Section
        with ui.column().classes(
            "w-full items-center pt-16 pb-20 px-4 bg-white scroll-animate-section"
        ):
            ui.label("COMMUNITY ACTION").classes(
                "text-base text-gray-500 font-serif tracking-widest"
            )
            ui.label("Upcoming Initiatives").classes(
                "text-3xl text-black font-bold mb-8 text-center"
            )

            with ui.column().classes("w-full max-w-3xl gap-4"):
                # Event 1
                with ui.row().classes(
                    "w-full items-center p-4 border rounded-lg shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-3 rounded-md mr-4"
                    ):
                        ui.label("JUL").classes("text-base font-bold text-black")
                        ui.label("25").classes("text-3xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Osu Community Cleanup Day").classes(
                            "text-xl font-bold"
                        )
                        ui.label("Oxford Street, Osu, Accra").classes(
                            "text-sm text-gray-600"
                        )
                    ui.button("Volunteer").props("color=black")

                # Event 2
                with ui.row().classes(
                    "w-full items-center p-4 border rounded-lg shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-3 rounded-md mr-4"
                    ):
                        ui.label("AUG").classes("text-base font-bold text-black")
                        ui.label("15").classes("text-3xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Town Hall Meeting on Public Safety").classes(
                            "text-xl font-bold"
                        )
                        ui.label("Online via Zoom").classes("text-sm text-gray-600")
                    ui.button("Join Meeting").props("color=black")

                # Event 3
                with ui.row().classes(
                    "w-full items-center p-4 border rounded-lg shadow-sm"
                ):
                    with ui.column().classes(
                        "items-center text-center bg-gray-100 p-3 rounded-md mr-4"
                    ):
                        ui.label("SEP").classes("text-base font-bold text-black")
                        ui.label("05").classes("text-3xl font-bold text-black")
                    with ui.column().classes("flex-grow"):
                        ui.label("Neighborhood Watch Training").classes(
                            "text-xl font-bold"
                        )
                        ui.label("East Legon Police Station").classes(
                            "text-sm text-gray-600"
                        )
                    ui.button("Register").props("color=black")

        # Customer Service Centers Section
        with ui.column().classes(
            "w-full items-center pt-16 pb-20 px-4 bg-gray-50 scroll-animate-section"
        ):
            ui.label("OUR PARTNERS").classes(
                "text-base text-gray-500 font-serif tracking-widest"
            )
            ui.label("Working With Government Authorities").classes(
                "text-3xl text-black font-bold mb-8 text-center"
            )

            with ui.row().classes("w-full max-w-4xl justify-center gap-x-12 gap-y-6"):
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
                        ui.label(authority).classes("text-base text-gray-600")

    # Manual "Back to Top" button for compatibility with all NiceGUI versions.
    # This button is controlled by the JavaScript and CSS added below.
    back_to_top_button = (
        ui.button(
            icon="arrow_upward",
            on_click=lambda: ui.run_javascript(
                "window.scrollTo({top: 0, behavior: 'smooth'})"
            ),
        )
        .props("fab color=black")
        .classes(
            "fixed bottom-8 right-8 z-50 opacity-0 transition-opacity duration-300"
        )
    )

    # Add JavaScript and CSS to control the button's visibility on scroll.
    # The button's ID is used to target it specifically.
    ui.add_head_html(
        f"""
        <style>
            /* When the 'show' class is added, the button becomes visible */
            #c{back_to_top_button.id}.show {{
                opacity: 1;
            }}
        </style>
        <script>
            window.addEventListener('scroll', function() {{
                const button = document.getElementById('c{back_to_top_button.id}');
                if (button) {{
                    // Show button if scrolled more than 200px, otherwise hide it
                    if (window.scrollY > 200) {{
                        button.classList.add('show');
                    }} else {{
                        button.classList.remove('show');
                    }}
                }}
            }});
        </script>
    """
    )

    show_footer()
