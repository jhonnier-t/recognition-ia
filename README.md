
---

## 🚀 Servicios

### 1. 🔀 FastAPI

- Maneja las rutas de entrada a los microservicios.
- Implementado con FastAPI.

### 2. 🧠 Recognition Service

- Servicio de IA que realiza tareas de transcripción y diarización de hablantes.
- Basado la API de gemini, usando las siguientes caracteristicas:
  - `audio_recognition`
  - `Gemini API`

### 3. 📡 Webhook Service

- Escucha peticiones POST de servicios externos (ej. Form Google).
- Procesa el archivo de audio.

### 4. 📦 Modules

- Contiene código reutilizable y módulos para la transcripción y diarización:
- Logger centralizado.
- Configuración del entorno.
- Validaciones comunes.

---

## 🐳 Docker Compose

```yaml
version: "3.9"

services:
  gateway:
    build: ./gateway
    ports:
      - "8000:8000"
    depends_on:
      - recognition
      - webhook

  recognition:
    build: ./recognition_service

  webhook:
    build: ./webhook_service
