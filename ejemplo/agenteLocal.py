import ollama

class AgenteLocal:
    def __init__(self, model= "gemma3:1b", system_prompt= "Eres un analista deportivo profesional, objetivo y didáctico. Tu misión es explicar y contextualizar el rendimiento de equipos y atletas, identificar claves tácticas y estadísticas, y presentar escenarios con sus justificaciones."):
        self.model = model
        self.messages = [{"role": "system", "content": system_prompt}]

    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        try:
            #Asignación de temperatura -> la alucinación
            options ={
                'temperature': 0.5
            }
            respuesta = ollama.chat(
                model= self.model,
                messages= self.messages,
                options= options
            )
            respuesta_asis = respuesta["message"]["content"]
            self.messages.append({"role": "assistant", "content": respuesta_asis})
            return respuesta_asis
        except Exception as e:
            return print(f"Error al generar la respuesta: {str(e)}")