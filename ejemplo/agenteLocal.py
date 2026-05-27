import ollama

class AgenteLocal:

    def __init__(
        self,
        model="gemma3:1b",
        system_prompt="",
        temperature=0.5
    ):

        self.model = model
        self.temperature = temperature

        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def chat(self, user_input):

        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        try:

            # Configuración del modelo
            options = {
                "temperature": self.temperature
            }

            respuesta = ollama.chat(
                model=self.model,
                messages=self.messages,
                options=options
            )

            respuesta_asis = respuesta["message"]["content"]

            # Guardar respuesta en historial
            self.messages.append(
                {
                    "role": "assistant",
                    "content": respuesta_asis
                }
            )

            return respuesta_asis

        except Exception as e:

            error_msg = f"ERROR: {str(e)}"

            print(error_msg)

            return error_msg