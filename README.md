# cisco-groq-evaredesava

**Generador Cisco con Groq.**

Herramienta de automatización basada en consola desarrollada en Python. Utiliza la API de Groq para transformar descripciones de red en comandos de configuración reales para equipos Cisco, optimizados para copiar y pegar directamente en la CLI.

👥 Integrantes y Roles
: Líder de Proyecto y Especialista en Seguridad (Configuración de .env y .gitignore).
: Desarrollador de Lógica y Validaciones.
: Documentación Técnica y Testing de Escenarios.

⚙️ Justificación de Parámetros del Modelo
Para cumplir con los estándares de producción en networking, se han configurado los siguientes parámetros en la API:
Temperature (0.2): Se utiliza un valor bajo para garantizar respuestas deterministas. Esto asegura que el modelo no "invente" sintaxis y proporcione comandos precisos y funcionales.
Max_tokens (800): Permite generar configuraciones completas y detalladas sin que la respuesta se corte prematuramente.
Modelo: Se utiliza "llama-3.3-70b-versatile" por su alta velocidad de respuesta y precisión en tareas técnicas.

🚀 Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual: "python -m venv venv".
3. Instalar dependencias: "pip install -r requirements.txt".
4. Configurar la API Key en un archivo ".env" local.

🛠️ Escenarios Soportados
Escenario A: Configuración de VLANs y Trunking.
Escenario B: Configuración de OSPF.
Escenario C: Subnetting y asignación de IPs[.

⚠️ Limitaciones
Requiere conexión a internet activa para realizar las consultas a la API de Groq.
Las validaciones actuales se limitan a rangos de VLAN y formato de direcciones IPv4.
