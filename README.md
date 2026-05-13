# eval-cisco-groq-tapia-cortes

**Generador de Configuraciones Cisco IOS con Inteligencia Artificial (Groq)**

Esta herramienta de consola en Python automatiza la creación de configuraciones para dispositivos Cisco (Routers y Switches). Utiliza el modelo de lenguaje **Llama-3.3-70b-versatile** a través de la API de Groq para transformar requerimientos técnicos en comandos precisos de Cisco IOS, listos para ser aplicados en entornos de red.

---

## 👥 Integrantes y Roles

* **José Tapia**: Líder de Proyecto. Responsable de la creación del repositorio base, estructuración de directorios y codificación de la arquitectura inicial del programa.
* **Martín Cortés**: Desarrollador Principal. Responsable del ajuste y optimización del código para el cumplimiento del 100% de los requerimientos técnicos, implementación de validaciones de red, generación de evidencias en `/configs` y redacción de la documentación técnica final.

---

## ⚙️ Justificación de Parámetros del Modelo

Para garantizar la fiabilidad necesaria en configuraciones de infraestructura de red, se han aplicado los siguientes parámetros técnicos conforme a la pauta:

1.  **Temperature (0.2)**: Se seleccionó un valor bajo para asegurar que la respuesta sea determinista y precisa. Esto garantiza que el modelo proporcione comandos estándar y funcionales, evitando "alucinaciones" en la sintaxis.
2.  **Max_tokens (800)**: Este límite asegura que se puedan generar configuraciones completas para escenarios complejos sin que el texto se corte prematuramente.
3.  **Stream (True)**: Requerimiento técnico obligatorio para visualizar la generación de comandos en tiempo real, mejorando la interacción en la consola.

---

## 🛠️ Escenarios Soportados y Ejemplos de Uso

El sistema está validado para los tres escenarios obligatorios:

### Escenario A: VLANs y Trunking
* **Entrada**: ID de VLAN (ej. 10), Nombre (ej. Ventas), Puertos (ej. fa0/1-5).
* **Resultado**: Genera la creación de la VLAN y la asignación de interfaces en modo acceso y troncal.

### Escenario B: OSPF
* **Entrada**: ID de proceso (ej. 1), Red y Wildcard (ej. 192.168.1.0 0.0.0.255), Área (ej. 0).
* **Resultado**: Genera el bloque `router ospf` con sus respectivas sentencias `network`.

### Escenario C: Subnetting e IPs
* **Entrada**: Red base con prefijo (ej. 172.16.0.0/16), Cantidad de subredes.
* **Resultado**: Realiza el cálculo de las subredes y genera los comandos `ip address` para las interfaces correspondientes.

---

## 🚀 Instalación y Configuración

### Requisitos
* Python 3.10+
* API Key de [Groq Cloud](https://console.groq.com/).

### Pasos
1.  **Clonar y preparar**:
    ```bash
    git clone [https://github.com/JoseTapia/cisco-groq-evaredesava.git](https://github.com/JoseTapia/cisco-groq-evaredesava.git)
    cd cisco-groq-evaredesava
    python -m venv .venv
    # Activar: .\.venv\Scripts\activate (Windows)
    pip install -r requirements.txt
    ```
2.  **Variables de Entorno**:
    Cree un archivo `.env` basado en `.env.example`:
    ```env
    GROQ_API_KEY=tu_clave_real_aqui
    ```

### Ejecución
```bash
python cisco_config_gen.py
