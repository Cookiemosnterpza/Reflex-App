"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                        ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                        ),
                        align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/prueba"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    rx.color_mode.button(position="top-right"),
                    justify="end",
                    spacing="5",
                    ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                        align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),     
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    ),


def prueba() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Registra tu cuenta",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Correo electronico",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="usuario_prueba@gmail.com",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Contraseña",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Ingresa tu contraseña",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Confirma contraseña",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Confirma tu contraseña",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Acepto Terminos y Condiciones",
                        default_checked=True,
                        spacing="2",
                    ),
                    width="100%",
                ),
                rx.button("Registrar", size="3", width="100%"),
                rx.center(
                    rx.text("Ya estas registrado?", size="3"),
                    rx.link("Ingresa aqui", href="#", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width="28em",
            size="4",
            width="100%",
        ),  
    )


app = rx.App()
app.add_page(index)
app.add_page(prueba, route="prueba")
