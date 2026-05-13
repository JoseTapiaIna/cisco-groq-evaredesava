# cisco-groq-evaredesava

**Generador de Configuraciones Cisco IOS con Inteligencia Artificial (Groq)**

Esta herramienta de consola en Python automatiza la creación de configuraciones para dispositivos Cisco (Routers y Switches). Utiliza el modelo de lenguaje **Llama-3.3-70b-versatile** a través de la API de Groq para transformar requerimientos técnicos en comandos precisos de Cisco IOS, listos para ser aplicados en entornos de red.

---

## 👥 Integrantes y Roles

* **José Tapia**: Líder de Proyecto. Responsable de la creación del repositorio base, estructuración de directorios y codificación de la arquitectura inicial del programa.
* **Martín Cortés**: Desarrollador Principal. Responsable del ajuste y optimización del código para el cumplimiento del 100% de los requerimientos técnicos, implementación de validaciones de red, generación de evidencias en `/configs` y redacción de la documentación técnica final.

---

## ⚙️ Justificación de Parámetros del Modelo

Para garantizar la fiabilidad necesaria en configuraciones de infraestructura de red, se han aplicado los siguientes parámetros técnicos conforme a la pauta:

1.  **Temperature (0.2)**: Se seleccionó un valor bajo para asegurar que la respuesta sea determinista y precisa. Esto minimiza la "creatividad" de la IA y garantiza que la sintaxis de los comandos sea estrictamente la estándar de Cisco.
2.  **Max_tokens (800)**: Este límite permite generar configuraciones extensas (como múltiples VLANs o procesos OSPF complejos) sin que la respuesta se vea truncada.
3.  **Stream (True)**: Requerimiento técnico obligatorio implementado para mejorar la experiencia de usuario, permitiendo visualizar la generación de la configuración en tiempo real en la consola.

---

## 🛠️ Escenarios Soportados (Mínimo Obligatorio)

El sistema está validado para generar configuraciones en tres áreas críticas de la pauta:

* **Escenario A: VLANs y Trunking**: Configuración de IDs de VLAN, nombres, asignación de puertos de acceso y configuración de enlaces troncales.
* **Escenario B: OSPF**: Configuración de procesos OSPF, declaración de redes, wildcards y asignación de áreas.
* **Escenario C: Subnetting e IPs**: Cálculo de subredes a partir de una red base y asignación de direcciones IP a interfaces.

---

## 🚀 Instalación y Uso

### Requisitos Previos
* Python 3.10 o superior.
* Una API Key válida de [Groq Cloud](https://console.groq.com/).

### Configuración
1.  **Clonar el repositorio**:
    ```bash
    git clone [https://github.com/JoseTapia/cisco-groq-evaredesava.git](https://github.com/JoseTapia/cisco-groq-evaredesava.git)
    cd cisco-groq-evaredesava
    ```
2.  **Crear y activar entorno virtual**:
    ```bash
    python -m venv .venv
    # En Windows:
    .\.venv\Scripts\activate
    ```
3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Variables de Entorno**:
    Cree un archivo `.env` en la raíz (use `.env.example` como referencia) y añada su llave:
    ```env
    GROQ_API_KEY=tu_clave_aqui
    ```

### Ejecución
```bash
python cisco_config_gen.py
