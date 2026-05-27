import ollama
import json

modelo = 'gemma3:1b'

schema = {
    "type": "object",
    "properties":{
        "sentimiento": {
            "type": "string",
            "enum": ["positivo", "negativo"]
        },
        "explicacion_breve": {
            "type": "string",
            "texto": ""
        }
    },
    "required": ["sentimiento"]
}

instruccion = "Eres un analizador de sentimiento. Analiza el siguiente texto y determina si el sentimiento es positivo o negativo, además de una breve explicación: "

prompt = input("Ingrese el texto a analizar: ")

respuesta = ollama.generate(
    model= modelo,
    prompt= instruccion + prompt,
    stream= False,
    format= schema,
    options= {"seed": 2}
)

#print(respuesta)
texto = respuesta['response']

print(f"Respuesta del modelo: {texto}")