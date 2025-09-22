# Como Publicar a AWS-API no Docker Hub

## Pré-requisitos

1. Conta no Docker Hub (<https://hub.docker.com>)
2. Docker instalado e funcionando
3. Imagem `aws-api:latest` já criada (✅ já temos)

## Passo a Passo

### 1. Fazer Login no Docker Hub

```bash
docker login
```

- Digite seu username do Docker Hub
- Digite seu password do Docker Hub

### 2. Criar Tag para o Docker Hub

**SUBSTITUA `SEU_USERNAME` pelo seu username do Docker Hub:**

```bash
# Formato: docker tag imagem-local username/repository:tag
docker tag aws-api:latest SEU_USERNAME/aws-api:latest
docker tag aws-api:latest SEU_USERNAME/aws-api:1.0.0
```

**Exemplo com username fictício:**

```bash
docker tag aws-api:latest lucasdev/aws-api:latest
docker tag aws-api:latest lucasdev/aws-api:1.0.0
```

### 3. Verificar as Tags Criadas

```bash
docker images | grep aws-api
```

### 4. Fazer Push para o Docker Hub

```bash
# Push da versão latest
docker push SEU_USERNAME/aws-api:latest

# Push da versão específica
docker push SEU_USERNAME/aws-api:1.0.0
```

### 5. Verificar no Docker Hub

- Acesse [https://hub.docker.com](https://hub.docker.com)
- Vá em "Repositories"
- Você deve ver `SEU_USERNAME/aws-api`

## Comandos Prontos (SUBSTITUA SEU_USERNAME)

```bash
# 1. Login
docker login

# 2. Tag (SUBSTITUA lucasdev pelo SEU username)
docker tag aws-api:latest lucasdev/aws-api:latest
docker tag aws-api:latest lucasdev/aws-api:1.0.0

# 3. Push (SUBSTITUA lucasdev pelo SEU username)
docker push lucasdev/aws-api:latest
docker push lucasdev/aws-api:1.0.0
```

## Como Outras Pessoas Vão Usar Sua Imagem

Depois de publicada, qualquer pessoa poderá usar sua imagem assim:

```bash
# Baixar e executar
docker run -d -p 8000:8000 SEU_USERNAME/aws-api:latest

# Ou especificar versão
docker run -d -p 8000:8000 SEU_USERNAME/aws-api:1.0.0
```

## Atualizações Futuras

Para publicar uma nova versão:

1. Faça as alterações no código
2. Rebuilde a imagem: `docker build -t aws-api:latest .`
3. Crie nova tag: `docker tag aws-api:latest SEU_USERNAME/aws-api:1.1.0`
4. Push: `docker push SEU_USERNAME/aws-api:1.1.0`

## Dicas Importantes

- **latest**: Sempre aponta para a versão mais recente
- **Versionamento**: Use tags como `1.0.0`, `1.1.0`, etc.
- **Repositório Público**: Por padrão, o repositório será público
- **Limite de Pulls**: Contas gratuitas têm limite de pulls por mês

## Exemplo de Dockerfile Hub Description

````markdown
# AWS FastAPI Application

Simple FastAPI application with two endpoints:

- `GET /ping` - Health check endpoint
- `GET /uppercase?text=your-text` - Convert text to uppercase

## Usage

```bash
docker run -d -p 8000:8000 SEU_USERNAME/aws-api:latest
```
````

## Test the API

```bash
curl http://localhost:8000/ping
curl "http://localhost:8000/uppercase?text=hello world"
```
