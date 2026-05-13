import os
import time
import re
from groq import Groq
from dotenv import load_dotenv

# 1. Cargar variables de entorno
load_dotenv()

# Configuración del cliente Groq
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("Error: La variable de entorno GROQ_API_KEY no está configurada.")
    print("Asegúrate de tener un archivo .env con tu llave.")
    exit(1)

client = Groq(api_key=api_key)

# --- FUNCIONES DE VALIDACIÓN (Eje 2: Calidad Técnica) ---

def validar_vlan(vlan_str):
    """Valida rango de VLAN 1-4094"""
    try:
        vlan = int(vlan_str)
        if 1 <= vlan <= 4094:
            return True
        print("❌ Error: ID de VLAN fuera de rango (1-4094).")
        return False
    except ValueError:
        print("❌ Error: La VLAN debe ser un número entero.")
        return False

def validar_ip_prefijo(ip_prefijo):
    """Valida formato IP/Prefijo (ej. 192.168.1.0/24)"""
    patron = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$"
    if re.match(patron, ip_prefijo):
        prefijo = int(ip_prefijo.split('/')[-1])
        if 8 <= prefijo <= 30:
            return True
        print("❌ Error: El prefijo debe estar entre /8 y /30.")
    else:
        print("❌ Error: Formato IP/Prefijo inválido (ej. 192.168.1.0/24).")
    return False

def validar_etherchannel(grupo_str):
    """Valida rango de Channel-group 1-255"""
    try:
        grupo = int(grupo_str)
        if 1 <= grupo <= 255:
            return True
        print("❌ Error: El número de grupo debe estar entre 1 y 255.")
        return False
    except ValueError:
        print("❌ Error: El grupo debe ser un número entero.")
        return False

# --- FUNCIÓN PRINCIPAL DE GENERACIÓN (Eje 1: Streaming e IA) ---

def generar_configuracion(prompt_usuario, tipo_escenario):
    """Envía el prompt a Groq con streaming y guarda la evidencia."""
    try:
        print(f"\n--- Generando Configuración para {tipo_escenario} ---\n")
        
        system_prompt = (
            "Eres un experto en networking certificado en Cisco CCNA y CCNP. "
            "Tu tarea es generar exclusivamente comandos de Cisco IOS. "
            "No des explicaciones largas, solo los bloques de comandos necesarios. "
            "Asegúrate de que la sintaxis sea 100% válida para Routers y Switches Cisco."
        )

        # Llamada a la API con Streaming (Eje 1.2)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.2, # Determinismo (Eje 1.4)
            max_tokens=800,
            stream=True
        )

        config_generada = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True) # Salida en tiempo real
                config_generada += content

        # Guardar en /configs (Eje 2.4: Persistencia)
        if not os.path.exists("configs"):
            os.makedirs("configs")
            
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        nombre_archivo = f"configs/{tipo_escenario}_{timestamp}.txt"
        
        with open(nombre_archivo, "w") as f:
            f.write(f"! Escenario: {tipo_escenario}\n")
            f.write(f"! Fecha: {timestamp}\n\n")
            f.write(config_generada)
            
        print(f"\n\n✅ Configuración guardada en: {nombre_archivo}")

    except Exception as e:
        print(f"\n❌ Error de API: {e}")

# --- MENÚ PRINCIPAL ---

def menu():
    while True:
        print("\n========================================")
        print("   CISCO CONFIG GENERATOR (GROQ IA)     ")
        print("      Integrantes: José y Martín        ")
        print("========================================")
        print("1. Escenario A: VLANs y Trunking")
        print("2. Escenario B: OSPF")
        print("3. Escenario C: Subnetting e IPs")
        print("4. Escenario D: EtherChannel (BONUS)")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            vlan_id = input("ID de la VLAN (1-4094): ")
            if validar_vlan(vlan_id):
                nombre = input("Nombre de la VLAN: ")
                puertos = input("Puertos de acceso (ej. fa0/1-10): ")
                trunk = input("Puerto Trunk (ej. gi0/1): ")
                prompt = f"Crea la VLAN {vlan_id} llamada {nombre}. Asigna los puertos {puertos} como acceso y el puerto {trunk} como trunk."
                generar_configuracion(prompt, "VLAN_Trunking")

        elif opcion == '2':
            proceso = input("ID de proceso OSPF: ")
            red = input("Red y Wildcard (ej. 192.168.1.0 0.0.0.255): ")
            area = input("Área: ")
            prompt = f"Configura router ospf {proceso}. Agrega la red {red} en el área {area}. Incluye router-id 1.1.1.1."
            generar_configuracion(prompt, "OSPF")

        elif opcion == '3':
            red_base = input("Red base con prefijo (ej. 10.0.0.0/8): ")
            if validar_ip_prefijo(red_base):
                subredes = input("¿Cuántas subredes necesitas?: ")
                prompt = f"Realiza un subnetting para la red {red_base} creando {subredes} subredes. Muestra la configuración de IP para las primeras 2 interfaces del router."
                generar_configuracion(prompt, "Subnetting")

        elif opcion == '4':
            grupo = input("Número de Channel-group (1-255): ")
            if validar_etherchannel(grupo):
                protocolo = input("Protocolo (LACP / PAgP / Manual): ")
                interfaces = input("Interfaces físicas (ej. gi0/1, gi0/2): ")
                prompt = f"Configura EtherChannel usando el protocolo {protocolo}. Channel-group {grupo} para las interfaces {interfaces}. Configura el Port-channel resultante."
                generar_configuracion(prompt, "EtherChannel")

        elif opcion == '5':
            print("Saliendo del programa... ¡Éxito en la defensa!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
