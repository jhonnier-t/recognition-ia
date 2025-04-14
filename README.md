
---
## 🚀 DOCS APP RECOGNITION IA
---
### 1. 🔀 FastAPI

- Manages incoming routes to the microservices.
- Built using FastAPI.

### `Curl is attached for testing the endpoint:`
```
curl --location 'http://127.0.0.1:8000/api/webhook/audio/upload' \
--form 'audio=@"/audio.ogg"' \
--form 'email="exmple@gmail.com"'
```
### `Params`
- `audio`: Audio file for recognition and segmentation.
- `email`: Mail to which you will be notified of the execution of the process.
---

### 2. 🧩 Qdrant Vector DB

Rationale Vector DB

- Easy to use and integrates very well with `Python` and `fastembed`.
- Allows to `store structured metadata` along with each vector (great for storing: filename, timestamp, speaker, etc.).
- `Open source` and has an official and `lighter Docker image`.
- Excellent support for semantic search with `metadata filtering`.
- Compatible with `OpenAI`, `fastembed`, `HuggingFace`, etc. embeddings.
- **HOST**:`http://localhost:6333/dashboard#/collections`

---

### 3. 🧠 Gemini API

- AI service for transcription and speaker diarization.
- Powered by the Gemini API with the following prompt:

```
Quiero que transcribas el siguiente audio en español y segmentes por hablante si es posible.
Sin texto adicional ni explicaciones. Devuélveme la respuesta en el siguiente formato:

Speaker = {"speaker": str, "time_stamp": "00:00:00.248", "text": str},
Return: list[Speaker]

⚠️ IMPORTANTE:

- No pongas la palabra json dentro de bloques de código (nada de json, ni ).
- No pongas las comillas hacia atrás ``` en el objeto JSON.
- No pongas salto de línea \n en el objeto JSON.
- No devuelvas caracteres de escape (nada de \", \\n, etc).
- No agregues ningún texto antes ni después del objeto JSON.
- No expliques nada, ni digas “Aquí tienes la transcripción” ni nada parecido.
- Devuelve solo la lista de objetos Speaker como JSON válido, limpio y directo.
- El texto debe estar sin errores y con puntuación correcta.
```

---

### 6. 🔄 n8n Integration

- **Purpose**: Automates workflows across the system.
- **Use Cases**:
  - Trigger transcriptions from external sources.
  - Send automated emails after transcription is completed.
  - Route outputs to third-party tools like Slack, Google Sheets, or CRMs.
- **Deployment**:
  - Easily deployable via Docker or hosted version.
  - Can connect to FastAPI endpoints to orchestrate task chains.
- **Execute workflow**:
  - `N8N_HOST`: URL for to execute workflow with FORM (e.g., `http://localhost:5678/`)
  - `CONFIGURATION FILE`: Contain config workflow`recognition_audio_workflow_n8n.json`


---

### 7. 🔍 ENV Variables

| Variable             | Required | Example                              |
|----------------------|----------|--------------------------------------|
| `GEMINI_API_KEY`     | ✅       | `your-google-api-key`               |
| `GEMINI_MODEL`       | ✅       | `gemini-2.5-pro-exp-03-25`          |
| `VECTOR_DB_PROVIDER`| ✅       | `qdrant`                             |
| `EMBEDDINGS_MODEL`   | ✅       | `BAAI/bge-small-en`                   |
| `SMTP_SERVER`        | ✅       | `smtp.gmail.com`                     |
| `SMTP_PORT`          | ✅       | `587`                                |
| `SENDER_EMAIL`       | ✅       | `example@gmail.com`                  |
| `SENDER_PASSWORD`    | ✅       | `Password123*`                       |

---

## 🐳 Docker Compose

```yaml
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

  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=admin123
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - WEBHOOK_TUNNEL_URL=http://localhost:5678
    volumes:
      - ./n8n_data:/home/node/.n8n

volumes:
  qdrant_storage:
    name: qdrant_storage
```
## `Deploy services docker execute command:` 
- ```docker-compose up -d --build```
---

