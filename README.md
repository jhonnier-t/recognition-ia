
---

## 🚀 Servicios

### 1. 🔀 FastAPI

- Maneja las rutas de entrada a los microservicios.
- Implementado con FastAPI.

### 2. 🧠 Recognition Service

- Servicio de IA que realiza tareas de transcripción y diarización de hablantes.
- Basado la API de gemini, usando las siguientes caracteristicas:
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
  qdrant:
    image: qdrant/qdrant:latest
    container_name: qdrant_container
    ports:
      - "6333:6333"
    volumes:
      - qdrant_storage:/qdrant/storage

  fastapi:
    build: .
    container_name: fastapi_container
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - qdrant
    environment:
      - QDRANT_HOST=${VECTOR_DB_PROVIDER}
      - QDRANT_PORT=6333
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - GEMINI_MODEL=${GEMINI_MODEL}
      - VECTOR_DB_PROVIDER=${VECTOR_DB_PROVIDER}

volumes:
  qdrant_storage:
    name: qdrant_storage
