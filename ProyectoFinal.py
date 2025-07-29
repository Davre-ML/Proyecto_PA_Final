"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import reflex.components as rxc
from reflex import State

from rxconfig import config

##pages
from Proyecto_PA_Final.pages.registro import registro
from Proyecto_PA_Final.pages.inicio_sesion import inicio_sesion

class State(rx.State):
    """The app state."""

    ...


    


app = rx.App()
app.add_page(inicio_sesion, route="/")
app.add_page(registro, route="/registro")

