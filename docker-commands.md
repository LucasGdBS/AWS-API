# Docker Commands for AWS-API

## Build the Docker image
```bash
docker build -t aws-api:latest .
```

## Run the container
```bash
docker run -d -p 8000:8000 --name aws-api-container aws-api:latest
```

## Run with environment variables (if needed)
```bash
docker run -d -p 8000:8000 --name aws-api-container \
  -e ENV_VAR_NAME=value \
  aws-api:latest
```

## Check container logs
```bash
docker logs aws-api-container
```

## Check container health
```bash
docker inspect aws-api-container --format='{{.State.Health.Status}}'
```

## Stop and remove container
```bash
docker stop aws-api-container
docker rm aws-api-container
```

## Test the API endpoints
```bash
# Health check
curl http://localhost:8000/ping

# Uppercase endpoint
curl "http://localhost:8000/uppercase?text=hello world"
```

## Multi-stage build alternative (optional)
If you want a smaller production image, you can modify the Dockerfile to use multi-stage builds:

```dockerfile
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY main.py .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```