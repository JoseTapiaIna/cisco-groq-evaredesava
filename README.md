# Cisco Config Generator (IA)

Este proyecto es un asistente inteligente basado en Inteligencia Artificial para la generación de configuraciones de red **Cisco IOS**. Utiliza el modelo **Llama-3.3-70b** a través de la API de **Groq** para automatizar tareas de administración de redes de forma rápida y precisa.

## 👥 Integrantes y Roles

* **José Tapia**: Líder de Proyecto. Responsable de la creación del repositorio base, estructuración de directorios y codificación de la arquitectura inicial del programa.
* **Martín Cortés**: Desarrollador Principal. Responsable del ajuste y optimización del código para el cumplimiento del 100% de los requerimientos técnicos, implementación de validaciones de red, generación de evidencias en `/configs` y redacción de la documentación técnica final.s

---

## 📋 Escenarios Implementados

El programa permite generar configuraciones para los siguientes casos de uso, garantizando sintaxis válida para equipos Cisco:

1.  **Escenario A: VLANs y Trunking:** Configuración de IDs, nombres, puertos de acceso y enlaces troncales (802.1Q).
2.  **Escenario B: OSPF:** Configuración de enrutamiento dinámico, IDs de proceso, redes, wildcards y áreas.
3.  **Escenario C: Subnetting e IPs:** Cálculo y asignación de direccionamiento IP basado en una red raíz y cantidad de subredes.
4.  **Escenario D: EtherChannel (Bonificación):** Agregación de enlaces mediante protocolos LACP, PAgP o modo manual, incluyendo la configuración de la interfaz lógica Port-channel.

---

## 🛠️ Justificación Técnica de Parámetros (Eje 1.4)

Para asegurar la fiabilidad de las configuraciones y evitar errores en entornos de producción, se configuraron los siguientes parámetros:

| Parámetro | Valor | Justificación |
| :--- | :--- | :--- |
| **Modelo** | `llama-3.3-70b-versatile` | Elegido por su alta capacidad de razonamiento lógico y precisión en sintaxis de programación y CLI. |
| **Temperature** | `0.2` | Un valor bajo que garantiza respuestas deterministas y técnicas, minimizando la creatividad del modelo para evitar comandos inexistentes. |
| **Max Tokens** | `800` | Extensión ideal para bloques de configuración completos sin riesgo de truncado de datos. |
| **System Prompt** | Restrictivo | Configurado para que el modelo actúe estrictamente como un experto CCNA/CCNP, entregando solo comandos sin explicaciones innecesarias. |

---

## 🔐 Seguridad y Calidad Técnica (Eje 2)

* **Gestión de Credenciales:** Uso de `python-dotenv` para evitar la exposición de la API Key. El archivo `.env` está protegido mediante `.gitignore`.
* **Validación Local:** Antes de realizar peticiones a la API, el script valida localmente parámetros como:
    * IDs de VLAN (1-4094).
    * Prefijos de red (8-30).
    * IDs de Channel-group (1-255).
* **Manejo de Errores:** Implementación de bloques `try/except` para capturar fallos de conexión, API keys faltantes o límites de tasa (Rate Limit 429).
* **Persistencia:** Todas las configuraciones generadas se almacenan automáticamente en la carpeta `/configs/` con marca de tiempo para auditoría.

---


Vale, aquí tienes el bloque completo y ordenado, listo para que lo copies y pegues de una sola vez en tu `README.md`.

```markdown
## 🚀 Instalación y Configuración

1. **Crear y activar entorno virtual:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate

```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


3. **Configurar variables de entorno:**
Cree un archivo `.env` en la raíz y añada su API Key:
```env
GROQ_API_KEY=tu_clave_de_groq_aqui

```


4. **Ejecutar el programa:**
```bash
python cisco_config_gen.py

```



---

## 📂 Estructura del Repositorio (Eje 3.2)

* **`cisco_config_gen.py`**: Código fuente principal.
* **`configs/`**: Repositorio local de configuraciones generadas (evidencia).
* **`.env.example`**: Guía para la configuración de variables de entorno.
* **`requirements.txt`**: Lista de librerías necesarias.
* **`.gitignore`**: Filtro de seguridad para archivos sensibles y temporales.

---

**© 2026 - Proyecto de Evaluación para Ingeniería en Telecomunicaciones.**

```

```

   
