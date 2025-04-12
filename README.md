
---
## 🚀 DOCS APP RECOGNITION IA
---
### 1. 🔀 FastAPI

- Manages incoming routes to the microservices.
- Built using FastAPI.

---

### 2. 🧩 Qdrant Vector DB

- Ideal for working with segmented text (supports structured payloads with metadata).
- Highly efficient for semantic search.
- Does not generate embeddings automatically, but integrates easily with externally generated ones.
- REST and gRPC support with straightforward Python integration.

---

### 3. 🧠 Recognition Service

- AI service for transcription and speaker diarization.
- Powered by the Gemini API with the following prompt:

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

### 4. 📡 Webhook Service

- Listens for external POST requests (e.g., from Google Forms).
- Processes the audio file accordingly.

---

### 5. 📦 Modules

- `email_module`: Handles email sending.
- `embeddings_module`: Handles vectorization using (text, metadata, vectors).
- `transcriber_module`: Handles transcription and speaker segmentation with Gemini.
- `vectorial_db_module`: Handles saving vectors to Qdrant.

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
- **Environment Variables** (optional if n8n is used):
  - `N8N_HOST`: URL or internal service name (e.g., `http://n8n:5678`)
  - `N8N_API_KEY`: API key for secure communication (if enabled)

---

### 7. ENV Variables

| Variable             | Required | Example                              |
|----------------------|----------|--------------------------------------|
| `GEMINI_API_KEY`     | ✅       | `your-google-api-key`               |
| `GEMINI_MODEL`       | ✅       | `gemini-2.5-pro-exp-03-25`          |
| `VECTOR_DB_PROVIDER`| ✅       | `qdrant`                             |
| `EMBEDDINGS_MODEL`   | ✅       | `all-MiniLM-L6-v2`                   |
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

