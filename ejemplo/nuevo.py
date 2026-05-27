from agenteLocal import AgenteLocal
from ejemplo import agenteLocal
from ejemplo import agenteLocal

sp_analista = (
"Eres un analista deportivo profesional, objetivo y didáctico. "
"Explica rendimiento, claves tácticas y estadísticas con claridad. "
"Sé conciso (2–3 frases) y termina cada turno con una pregunta dirigida al otro agente. "
"No inventes datos; si faltan, dilo y explica los supuestos."
)

sp_biologo = (
"Eres un biólogo con enfoque en comunicación científica clara y rigurosa. "
"Relaciona conceptos biológicos relevantes con el tema, explica procesos de forma accesible. "
"Sé conciso (2–3 frases) y termina cada turno con una pregunta dirigida al otro agente. "
"No inventes datos; si faltan, dilo y explica los supuestos."
)

agente_deporte = AgenteLocal(system_prompt=sp_analista) # personalidad vía system_prompt 
agenteLocal.py

agente_bio = AgenteLocal(system_prompt=sp_biologo)

tema = input("Tema de la conversación: ")
turnos_max = 8

mensaje_a = f"Tema: {tema}. Inicia el diálogo cumpliendo las reglas."

for i in range(turnos_max):
# Turno del analista deportivo
    resp_a = agente_deporte.chat(mensaje_a) # conserva historial y contexto 
    agenteLocal.py

    print(f"Analista deportivo: {resp_a}")

    if "FIN" in resp_a.upper():
        break

    # Turno del biólogo (recibe lo que dijo el analista)
    resp_b = agente_bio.chat(resp_a)
    print(f"Biólogo: {resp_b}")

    if "FIN" in resp_b.upper():
        break

    # Lo que dijo el biólogo pasa a ser la siguiente entrada del analista
    mensaje_a = resp_b