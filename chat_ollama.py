import ollama
from ejemplo.agenteLocal import AgenteLocal

mi_agente = AgenteLocal()
print("Agente cody banks está listo")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("El agente cody banks se despide!")
        break
    respuesta = mi_agente.chat(user_input)
    print(f"Agente cody banks: {respuesta}")

#Cambiar contexto a experto en c++
sp = "Eres un experto en c++, responde a mis preguntas con un carácter profesional siendo conciso."
mi_agente = AgenteLocal(system_prompt=sp)
print("Agente C++ está listo")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("El agente C++ se despide!")
        break
    respuesta = mi_agente.chat(user_input)
    print(f"Agente C++: {respuesta}")

#Agente experto en python
sp = "Eres un experto en Python, responde a mis preguntas con un carácter profesional siendo conciso."
mi_agente = AgenteLocal(system_prompt=sp)
print("Agente Python está listo")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("El agente Python se despide!")
        break
    respuesta = mi_agente.chat(user_input)
    print(f"Agente Python: {respuesta}")