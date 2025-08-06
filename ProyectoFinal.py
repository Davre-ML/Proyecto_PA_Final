"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import reflex.components as rxc
from reflex import State

from rxconfig import config

#------------------PAGES------------------#
from ProyectoFinal.pages.registro import registro
from ProyectoFinal.pages.inicio_sesion import inicio_sesion
#--------------------------------------------#

class State(rx.State):
    """The app state."""

    ...


    
#------------------HOME------------------#    

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Projects", "square-library", "/#"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )


def side_bar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.icon_button(
                        rx.icon("user"),
                        size="3",
                        radius="full",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "David Morales",
                                size="3",
                                weight="bold",
                            ),
                            rx.text(
                                "davidmlopez123@gmail.com",
                                size="2",
                                weight="medium",
                            ),
                            width="100%",
                        ),
                        spacing="0",
                        justify="start",
                        width="100%",
                    ),
                    rx.spacer(),
                    rx.icon_button(
                        rx.icon("settings"),
                        size="2",
                        variant="ghost",
                        color_scheme="gray",
                    ),
                    padding_x="0.5rem",
                    align="center",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                sidebar_item(
                    "Help & Support", "life-buoy", "/#"
                ),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                #height="200%",
                height="780px",
                width="22em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                sidebar_item(
                                    "Help & Support",
                                    "life-buoy",
                                    "/#",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "My account",
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                "user@reflex.dev",
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )

def cards() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.card(
                rx.vstack(
                    rx.text("Usuario 1", size="3", weight="bold"),
                    rx.text("Historia", size="2", weight="medium"),
                    rx.text("Alguien sabe cuando inicio la revolución francesa?", size="2", weight="medium"),
                ),
                width="100%",
                padding="1em",
                bg=rx.color("accent", 3),
                border_radius="0.5em",
            ),
            rx.button(
                "Responder",
                width="100%",
                ),
            rx.card(
                rx.vstack(
                    rx.text("Usuario 2", size="3", weight="bold"),
                    rx.text("Historia", size="2", weight="medium"),
                    rx.text("Alguien sabe cuando termino la revolución francesa?", size="2", weight="medium"),
                ),
                width="100%",
                padding="1em",
                bg=rx.color("accent", 3),
                border_radius="0.5em",
            ),
            rx.button(
                "Responder",
                width="100%",
                ),
            rx.card(
                rx.vstack(
                    rx.text("Usuario 3", size="3", weight="bold"),
                    rx.text("Historia", size="2", weight="medium"),
                    rx.text("Alguien sabe cuando inicio la revolucion industrial?", size="2", weight="medium"),
                ),
                width="100%",
                padding="1em",
                bg=rx.color("accent", 3),
                border_radius="0.5em",
            ),
            rx.button(
                "Responder",
                width="100%",
                ),
            rx.card(
                rx.vstack(
                    rx.text("Usuario 1", size="3", weight="bold"),
                    rx.text("Historia", size="2", weight="medium"),
                    rx.text("Alguien sabe cuando inicio la revolución francesa?", size="2", weight="medium"),
                ),
                width="100%",
                padding="1em",
                bg=rx.color("accent", 3),
                border_radius="0.5em",
            ),
            rx.button(
                "Responder",
                width="100%",
                ),
        ),
        spacing="2",
        width="100%",
    )
def home() -> rx.Component:
    return rx.hstack(
        side_bar(),
        rx.vstack(
            rx.box(
                rx.text("Home", size="5", weight="bold"),
                width="100%",
                padding="1em",
            ),
        rx.scroll_area(
            cards(),
            spacing="2",
            width="100%",
            padding_x="1em",
            )
        ),
        width="100%",
        height="100%",
    )
    
    
app = rx.App()
app.add_page(inicio_sesion, route="/")
app.add_page(registro, route="/registro")
app.add_page(home, route="/home")

