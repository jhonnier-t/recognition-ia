
---

## 🚀 Servicios

### 1. 🔀 FastAPI

- Maneja las rutas de entrada a los microservicios.
- Implementado con FastAPI.

---

### 2. 🧩 Qdrant Vectorial BD
- Excelente para usar con textos segmentados (permite payloads estructurados con metadatos).
- Altamente eficiente para búsqueda semántica.
- No genera embeddings automáticamente, pero es muy amigable con embeddings generados externamente.
- Soporte REST y gRPC, integración muy sencilla desde Python.

---

### 3. 🧠 Recognition Service

- Servicio de IA que realiza tareas de transcripción y diarización de hablantes.
- Basado la API de gemini, usando el siguiente `Prompt`:
```
Quiero que transcribas el siguiente audio en español y segmentes por hablante si es posible. 
Sin texto adicional ni explicaciones. Devuélveme la respuesta en el siguiente formato:

Speaker = {"speaker": str, "time_stamp": "00:00:00.248", "text": str},
Return: list[Speaker]

⚠️ IMPORTANTE:
- No pongas el JSON dentro de bloques de código (nada de ```json ni ```).
- No agregues ningún texto antes ni después del JSON.
- No expliques nada, ni digas “Aquí tienes la transcripción” ni nada parecido.
- Solo devuelve el JSON puro, exactamente con ese formato.
- No devuelvas el JSON como una cadena (nada de escapado con \").
```
---

### 4. 📡 Webhook Service

- Escucha peticiones POST de servicios externos (ej. Form Google).
- Procesa el archivo de audio.

---

### 5. 📦 Modules

- `email_module` Contiene el envio de email
- `embeddings_module` Contiene la vectorización con (texto, metadatos, vectores) embeddings 
- `transcriber_module` Contiene la transcipcion y segementacion con Gemini
- `vectorial_db_module` Contiene el guardado de los vectores con Qdrant

---

### 6. ENV variables
- GEMINI_API_KEY -> `Obligatorio`, API KEY generada desde Google. (https://aistudio.google.com/app/apikey)
- GEMINI_MODEL -> `Obligatorio`, ejemplo: `gemini-2.5-pro-exp-03-25`
- VECTOR_DB_PROVIDER -> `Obligatorio`, ejemplo: `qdrant`
- EMBEDDINGS_MODEL -> `Obligatorio`, ejemplo: `"all-MiniLM-L6-v2"`
- SMTP_SERVER -> `Obligatorio`, ejemplo: `smtp.gmail.com`
- SMTP_PORT -> `Obligatorio`, ejemplo: `587` ,
- SENDER_EMAIL -> `Obligatorio`, ejemplo: `exmple@gmail.com`
- SENDER_PASSWORD -> `Obligatorio`, ejemplo: `Password123*`

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
      - QDRANT_HOST=qdrant
      - QDRANT_PORT=6333
      - GEMINI_MODEL=${GEMINI_MODEL}
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - VECTOR_DB_PROVIDER=${VECTOR_DB_PROVIDER}
      - EMBEDDINGS_MODEL=${EMBEDDINGS_MODEL}
      - SMTP_SERVER=${SMTP_SERVER}
      - SMTP_PORT=${SMTP_PORT}
      - SENDER_EMAIL=${SENDER_EMAIL}
      - SENDER_PASSWORD=${SENDER_PASSWORD}

volumes:
  qdrant_storage:
    name: qdrant_storage
