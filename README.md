# Word Replacement LLM with Ollama

This repository provides a FastAPI server that leverages the Ollama language model for LLM inferences on CPU. The server can be run in a Docker container, and it includes a background thread to keep the model active, ensuring quick inference times. The purpose of the project is to get replacements for words while keeping the context and symantics intact

## Features

- **Ollama Language Model**: Utilizes the Ollama model for LLM inferences on CPU.
- **FastAPI**: A lightweight and fast web framework for building APIs.
- **Threading**: Maintains model activity with a background thread that makes periodic calls.
- **Docker Support**: Easily deploy the application using Docker.

## Getting Started

### Running the Application

1. **Prerequisits**

- Docker installed on your machine.

2. **Build the Docker Image**

   ```bash
   docker build -t word-replacer-image .
   ```

3. **Run the Docker Container**

   ```bash
   docker run -p 5000:5000 word-replacer-image
   ```

   The application will be accessible at `http://127.0.0.1:5000/docs`.

### API Endpoints

- **GET /**: Check if the server is running.

   **Example Response**:
   ```json
   {
       "status": "Server is running!"
   }
   ```

- **POST /replace_word**: Replace a specific word in a given context.

   **Request Body**:
   ```json
   {
       "word_to_replace": "word",
       "context": "This is the context of the sentence."
   }
   ```

   **Example Response**:
   ```json
   {
       "replacement": "replacement_word",
       "time": "0.123"
   }
   ```

### Dockerfile Overview

The `Dockerfile` sets up the environment for the FastAPI server:

- **Base Image**: Uses `python:3.10-slim`.
- **Environment Variables**: Sets `DEBIAN_FRONTEND=noninteractive` for non-interactive installs.
- **Dependencies**: Installs necessary packages, including `curl` and Python packages (`ollama`, `fastapi`, `uvicorn`).
- **Working Directory**: Sets the working directory to `/app` and copies the application code.
- **Startup Command**: Runs the `start_services.sh` script to start the Ollama model and the FastAPI server.

### Keeping the Model Active

The application includes a heartbeat function that makes a call to the Ollama model every minutes. This keeps the model warm, allowing for faster responses to user requests. The call uses placeholder data to ensure that the model remains active without unnecessary computations.

### Example Usage

You can test the API using tools like `curl` or Postman.

#### Example `curl` command for replacing a word:

```bash
curl -X POST "http://127.0.0.1:5000/replace_word" \
-H "Content-Type: application/json" \
-d '{"word_to_replace": "cyber", "context": "In the world of technology, cyber attacks are a common threat."}'
```

## Contact
Author: Turyal Neeshat
Contact: tneeshat@outlook.com
