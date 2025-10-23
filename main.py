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
    ui.add_head_html(
        """
        <style>
            /* Initial state for elements that will animate */
            .scroll-animate-section {
                opacity: 0;
                transform: translateY(20px); /* Start slightly below its final position */
                transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Smooth transition */
            }
            /* Override browser's default autofill style */
            input:-webkit-autofill,
            input:-webkit-autofill:hover,
            input:-webkit-autofill:focus,
            input:-webkit-autofill:active {                
                transition: background-color 5000s ease-in-out 0s;
                -webkit-box-shadow: 0 0 0 30px white inset !important;
                -webkit-text-fill-color: #000 !important;
            }
            /* Final state when element is in view */
            .scroll-animate-section.scroll-animate-active {
                opacity: 1;
                transform: translateY(0);
            }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const sections = document.querySelectorAll('.scroll-animate-section');
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('scroll-animate-active');
                            // Optionally, stop observing once animated if you don't want re-animation on scroll up/down
                            // observer.unobserve(entry.target);
                        }
                    });
                }, { threshold: 0.1 }); // Trigger when 10% of the element is visible
                sections.forEach(section => { observer.observe(section); });
            });
        </script>
    """
    )

    show_home()


ui.run(storage_secret="tgdsgdyudjjsijd")
