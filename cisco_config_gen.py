import os
import time
import re
from groq import Groq
from dotenv import load_dotenv

# 1. Cargar variables de entorno [cite: 25]
load_dotenv()

# Configuración del cliente Groq [cite: 25]
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("Error: La variable de entorno GROQ_API_KEY no está configurada.")
    exit(1)

client = Groq(api_key=api_key)

# --- FUNCIONES DE VALIDACIÓN (Requerimiento 2.3.5)  ---

def validar_vlan(vlan_str):
    """Valida rango de VLAN 1-4094 [cite: 31]"""
    try:
        vlan = int(vlan_str)
        return 1 <= vlan <= 4094
    except ValueError:
        return False

def validar_ip_prefijo(ip_prefijo):
    """Valida prefijos /8 a /30 [cite: 31]"""
    patron = r"^\d{1,3}(\.\d{1,3}){3}/(\d+)$"
    match = re.match(patron, ip_prefijo)
    if match:
        prefijo = int(match.group(2))
        return 8 <= prefijo <= 30
    return False

# --- MOTOR DE GENERACIÓN ---

def generar_configuracion(prompt_usuario, escenario_tipo):
    # System Prompt especializado [cite: 29]
    system_prompt = (
        "Eres un experto en Cisco IOS. Devuelve SOLO comandos válidos. "
        "Sin explicaciones, sin texto extra. Formato de bloque listo para copiar y pegar. "
        "Usa '!' para comentarios si es necesario."
    )

    try:
        # Llamada con streaming (Requerimiento 2.3.2) [cite: 27]
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.2, # Determinístico 
            max_tokens=800,  # 
            stream=True,
        )

        config_acumulada = ""
        print(f"\n--- Generando Configuración: {escenario_tipo} ---")
        for chunk in stream:
            if chunk.choices[0].delta.content:
                texto = chunk.choices[0].delta.content
                print(texto, end="")
                config_acumulada += texto

        # Persistencia en /configs/ [cite: 30, 41]
        if not os.path.exists('configs'): 
            os.makedirs('configs')
            
        nombre_archivo = f"configs/escenario_{escenario_tipo}_{int(time.time())}.txt"
        with open(nombre_archivo, "w") as f:
            f.write(config_acumulada)
        print(f"\n\n[OK] Configuración guardada en: {nombre_archivo}")

    # Manejo de errores específicos (Requerimiento 2.3.6) 
    except Exception as e:
        if "429" in str(e):
            print("\n[Error] Límite de tasa excedido (Rate Limit). Espere un momento.")
        elif "API key" in str(e):
            print("\n[Error] API Key inválida o faltante.")
        else:
            print(f"\n[Error de Red/API]: {e}")

# --- MENÚ PRINCIPAL ---

def main():
    while True:
        print("\n=== GENERADOR CISCO IOS (INACAP) ===")
        print("1. Escenario A: VLANs y Trunking")
        print("2. Escenario B: OSPF")
        print("3. Escenario C: Subnetting e IPs")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            vlan = input("Ingrese ID de VLAN (1-4094): ")
            if validar_vlan(vlan):
                nombre = input("Nombre de la VLAN: ")
                puertos = input("Puertos asignados (ej. fa0/1-5): ")
                prompt = f"Configura la VLAN {vlan} llamada {nombre} y asigna los puertos {puertos} como acceso. También configura trunk en g0/1."
                generar_configuracion(prompt, "VLAN_Trunking")
            else:
                print("[Error] ID de VLAN fuera de rango. No se consumió API.")

        elif opcion == "2":
            ospf_id = input("ID de proceso OSPF (numérico): ")
            if ospf_id.isdigit():
                red = input("Red a anunciar (ej. 192.168.1.0 0.0.0.255): ")
                area = input("Área: ")
                prompt = f"Configura OSPF proceso {ospf_id}, anuncia la red {red} en el área {area}."
                generar_configuracion(prompt, "OSPF")
            else:
                print("[Error] El ID de OSPF debe ser un número.")

        elif opcion == "3":
            red_base = input("Red base con prefijo (ej. 192.168.1.0/24): ")
            if validar_ip_prefijo(red_base):
                subredes = input("Cantidad de subredes requeridas: ")
                prompt = f"Realiza subnetting de {red_base} para obtener {subredes} subredes. Muestra la configuración de IP para las primeras interfaces."
                generar_configuracion(prompt, "Subnetting")
            else:
                print("[Error] Prefijo inválido (use entre /8 y /30).")

        elif opcion == "4":
            print("Cerrando programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
