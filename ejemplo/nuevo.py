from agenteLocal import AgenteLocal


# =========================
# PROMPTS DE LOS AGENTES
# =========================

sp_analista = (
    "Eres un analista deportivo profesional. "
    "Habla sobre estrategia, rendimiento y estadísticas. "
    "Máximo 3 frases y menos de 100 palabras. "
    "No uses la palabra FIN a menos que quieras terminar la conversación. "
    "Termina con una pregunta para el siguiente agente."
)

sp_biologo = (
    "Eres un biólogo experto en comunicación científica. "
    "Relaciona el tema con biología, evolución y naturaleza. "
    "Máximo 3 frases y menos de 100 palabras. "
    "No uses la palabra FIN a menos que quieras terminar la conversación. "
    "Termina con una pregunta para el siguiente agente."
)

sp_ingeniero = (
    "Eres un ingeniero especializado en sistemas y tecnología. "
    "Analiza el tema desde un enfoque técnico y funcional. "
    "Máximo 3 frases y menos de 100 palabras. "
    "No uses la palabra FIN a menos que quieras terminar la conversación. "
    "Termina con una pregunta para el siguiente agente."
)

sp_historiador = (
    "Eres un historiador experto en evolución histórica y contexto social. "
    "Relaciona el tema con hechos históricos relevantes. "
    "Máximo 3 frases y menos de 100 palabras. "
    "No uses la palabra FIN a menos que quieras terminar la conversación. "
    "Termina con una pregunta para el siguiente agente."
)

sp_psicologo = (
    "Eres un psicólogo especializado en comportamiento humano. "
    "Analiza emociones, motivaciones y conductas relacionadas con el tema. "
    "Máximo 3 frases y menos de 100 palabras. "
    "No uses la palabra FIN a menos que quieras terminar la conversación. "
    "Termina con una pregunta para el siguiente agente."
)

# AGENTE OBSERVADOR
sp_observador = (
    "Eres un observador neutral de conversaciones multiagente. "
    "Analiza toda la conversación entre los agentes. "
    "Genera un resumen general de la interacción. "
    "Verifica si siguieron correctamente el tema principal. "
    "Identifica cuál agente se salió más del tema y explica por qué. "
    "Menciona qué agentes aportaron mejor información. "
    "Sé objetivo, claro y organizado."
)


# =========================
# CREACIÓN DE AGENTES
# =========================

agente_deporte = AgenteLocal(
    system_prompt=sp_analista,
    temperature=0.8
)

agente_bio = AgenteLocal(
    system_prompt=sp_biologo,
    temperature=0.5
)

agente_ingeniero = AgenteLocal(
    system_prompt=sp_ingeniero,
    temperature=0.6
)

agente_historiador = AgenteLocal(
    system_prompt=sp_historiador,
    temperature=0.7
)

agente_psicologo = AgenteLocal(
    system_prompt=sp_psicologo,
    temperature=0.9
)

# SEXTO AGENTE OBSERVADOR
agente_observador = AgenteLocal(
    system_prompt=sp_observador,
    temperature=0.3
)


# =========================
# LISTA DE AGENTES
# =========================

agentes = [
    ("Analista Deportivo", agente_deporte),
    ("Biólogo", agente_bio),
    ("Ingeniero", agente_ingeniero),
    ("Historiador", agente_historiador),
    ("Psicólogo", agente_psicologo)
]


# =========================
# CONFIGURACIÓN
# =========================

tema = input("Tema de la conversación: ")

turnos_max = 3

mensaje_actual = (
    f"Tema principal: {tema}. "
    "Inicia la conversación cumpliendo todas tus reglas."
)


# =========================
# HISTORIAL GLOBAL
# =========================

historial_conversacion = ""

conversacion_terminada = False


# =========================
# CONVERSACIÓN MULTIAGENTE
# =========================

for turno in range(turnos_max):

    print(f"\n========== TURNO {turno + 1} ==========\n")

    for nombre, agente in agentes:

        respuesta = agente.chat(mensaje_actual)

        print(f"########## {nombre} ##########")
        print(respuesta)
        print()

        # Guardar historial
        historial_conversacion += (
            f"{nombre}:\n"
            f"{respuesta}\n\n"
        )

        # Validación
        if respuesta is None:

            print("Error: respuesta vacía")
            continue

        # Revisar FIN
        if "FIN" in respuesta.upper():

            conversacion_terminada = True

        # La respuesta pasa al siguiente agente
        mensaje_actual = respuesta

    # TERMINAR DESPUÉS
    # DE QUE TODOS HABLEN
    if conversacion_terminada:

        print("\nConversación finalizada.\n")
        break


# =========================
# ANÁLISIS FINAL
# =========================

print("\n===================================")
print("########## OBSERVADOR ##########")
print("===================================\n")

prompt_observador = f"""
Tema principal:
{tema}

Conversación completa:
{historial_conversacion}

Realiza lo siguiente:

1. Resume la conversación.
2. Explica cómo interactuaron los agentes.
3. Determina si siguieron correctamente el tema principal.
4. Identifica qué agente se salió más del tema.
5. Explica por qué se salió del tema.
6. Indica cuáles agentes dieron las mejores aportaciones.
7. Evalúa la calidad general de la conversación.
"""

analisis_final = agente_observador.chat(prompt_observador)

print(analisis_final)