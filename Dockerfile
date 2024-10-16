FROM python:3.10-slim

# Set environment variables to ensure non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y curl

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Python dependencies
RUN pip3 install ollama fastapi uvicorn

# Set working directory
WORKDIR /app

# Copy current directory to working directory
COPY . .

# Make the script executable
RUN chmod +x start_services.sh

# Expose port 5000 for API access
EXPOSE 5000

# Define default command
CMD ["./start_services.sh"]
