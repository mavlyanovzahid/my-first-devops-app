# Use a lightweight Python image
FROM python:3.12-slim

# Security: Create a non-root user to run the app
RUN useradd -m devopsuser
USER devopsuser

WORKDIR /app

# Copy your app script into the container
COPY app.py .

# Tell the container to listen on port 8080
EXPOSE 8080

# The command to start your app
CMD ["python", "app.py"]
