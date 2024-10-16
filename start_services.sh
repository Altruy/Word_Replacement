#!/bin/bash

# Start ollama serve in the background and redirect output to /dev/null
ollama serve > /dev/null 2>&1 &

# Wait for a few seconds to ensure the server is ready
sleep 5

# Pull the llama3 model
# ollama pull llama3
ollama pull gemma2:2b

# Start the FastAPI server with uvicorn
uvicorn main:app --host 0.0.0.0 --port 5000
