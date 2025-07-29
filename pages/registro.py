import reflex as rx
from reflex import State
from rxconfig import config


def registro() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.center(
                    rx.container(
                        rx.heading("Student Overview", size="9", color="black"),
                        padding="200px",
                    ),
                ),
                width="50vw",
                height="100vh",
                bg="#FFFFFF",
            ),
            rx.box(
                rx.box(
                    width="15vw",
                height="25vh",
                bg="#FFFFFF",
                ),
                rx.center(
                    rx.card(
                        rx.vstack(
                            rx.center(
                                rx.heading(
                                    "Crea tu cuenta",
                                    size="6",
                                    as_="h2",
                                    text_align="center",
                                    width="100%",
                                ),
                                direction="column",
                                spacing="5",
                                width="100%",
                            ),
                            rx.vstack(                      #NOMBRE
                                rx.text(
                                    "Nombre",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="user123",
                                    type="nombre",
                                    size="3",
                                    width="100%",
                                ),
                                justify="start",
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Correo electrónico",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="user@gmail.com",
                                    type="email",
                                    size="3",
                                    width="100%",
                                ),
                                justify="start",
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.text(
                                        "Contraseña",
                                        size="3",
                                        weight="medium",
                                    ),
                                    justify="between",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="Ingresa tu contraseña",
                                    type="password",
                                    size="3",
                                    width="100%",
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.button("Crear", size="3", width="100%"),
                            spacing="6",
                            width="100%",
                        ),
                        size="4",
                        max_width="28em",
                        width="100%",
                        padding="4",
                        shadow="md",
                    ),
                padding="4",
                ),
                width="50vw",
                height="100vh",
                bg="#FFFFFF",
            ),
        ),
    ) 
