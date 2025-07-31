import reflex as rx
from .database import insert_data
from .auth import AuthState # Necesitamos el ID y nombre del usuario logueado

class QuestionState(rx.State):
    """Estado para manejar la creación de preguntas."""
    question_text: str = ""
    materia: str = ""
    post_success: bool = False
    error_message: str = ""

    def set_question_text(self, text: str):
        self.question_text = text

    def set_materia(self, materia: str):
        self.materia = materia

    async def post_question(self):
        """
        Sube una nueva pregunta a la tabla 'preguntas'.
        Asegura que el usuario esté logueado y que los datos sean válidos.
        """
        self.error_message = ""
        self.post_success = False

        if not AuthState.is_logged_in:
            self.error_message = "Debes iniciar sesión para publicar una pregunta."
            return rx.redirect("/login")

        if not self.question_text or not self.materia:
            self.error_message = "Por favor, ingresa el texto de la pregunta y la materia."
            return

        # Recuperar el ID y nombre del usuario logueado desde AuthState
        user_id = AuthState.current_user_id
        user_name = AuthState.current_user_name

        if not user_id or not user_name:
            self.error_message = "Error: No se pudo obtener la información del usuario logueado."
            return

        question_data = {
            "pregunta_text": self.question_text,
            "user_id": user_id,
            "materia": self.materia,
            "nombre_user": user_name,
            # created_at se puede manejar automáticamente por Supabase con un DEFAULT current_timestamp
        }

        inserted_question = await insert_data("preguntas", question_data)

        if inserted_question:
            self.post_success = True
            self.error_message = "Pregunta publicada exitosamente."
            self.question_text = "" # Limpiar el campo
            self.materia = "" # Limpiar el campo
        else:
            self.error_message = "Error al publicar la pregunta. Inténtalo de nuevo."


def create_question_page():
    """Página para crear una nueva pregunta."""
    return rx.center(
        rx.vstack(
            rx.heading("Hacer una Pregunta", size="7"),
            rx.text(f"Usuario: {AuthState.current_user_name}", size="4"),
            rx.input(
                placeholder="Escribe tu pregunta aquí...",
                on_blur=QuestionState.set_question_text,
                value=QuestionState.question_text, # Para limpiar el campo después de publicar
                width="100%"
            ),
            rx.input(
                placeholder="Materia (ej. Matemáticas, Historia)",
                on_blur=QuestionState.set_materia,
                value=QuestionState.materia, # Para limpiar el campo
                width="100%"
            ),
            rx.button("Publicar Pregunta", on_click=QuestionState.post_question),
            rx.cond(QuestionState.error_message, rx.text(QuestionState.error_message, color="red")),
            rx.cond(QuestionState.post_success, rx.text("¡Pregunta publicada!", color="green")),
            rx.link("Volver al inicio", href="/"),
        ),
        height="100vh",
        width="600px", # Limitar ancho para mejor visualización
        padding="20px"
    )
