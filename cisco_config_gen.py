import os
import time
from groq import Groq
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Requerimiento: Leer desde variable de entorno [cite: 25]
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generar_configuracion(prompt_usuario, escenario_tipo):
    # ÍTEM 6: System Prompt especializado [cite: 29, 52]
    system_prompt = (
        "Eres un experto en Cisco IOS. Devuelve SOLO comandos válidos. "
        "Sin explicaciones, sin texto extra. Formato de bloque listo para copiar y pegar. "
        "Usa '!' para comentarios si es necesario."
    )

    try:
        # Requerimiento: stream=True para tiempo real [cite: 27]
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.2, # Requerimiento: determinístico [cite: 34]
            stream=True,
        )

        config_acumulada = ""
        print(f"\n--- Generando Escenario: {escenario_tipo} ---")
        for chunk in stream:
            if chunk.choices[0].delta.content:
                texto = chunk.choices[0].delta.content
                print(texto, end="")
                config_acumulada += texto

        # Requerimiento: Persistencia en carpeta /configs/ [cite: 30, 41]
        if not os.path.exists('configs'): os.makedirs('configs')
        nombre_archivo = f"configs/escenario_{escenario_tipo}_{int(time.time())}.txt"
        with open(nombre_archivo, "w") as f:
            f.write(config_acumulada)

    except Exception as e:
        print(f"Error: {e}")

def main():
    # Estructura de menú inicial 
    print("1. Escenario A: VLANs y Trunking")
    print("2. Escenario B: OSPF")
    print("3. Escenario C: Subnetting")
    opcion = input("Seleccione escenario: ")
    # Aquí irán las validaciones en la Sesión 2 [cite: 31]
    generar_configuracion("Prueba de prompt", "A")

if __name__ == "__main__":
    main()
