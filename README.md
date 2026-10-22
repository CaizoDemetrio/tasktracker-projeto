# TaskTracker - Fase 2
Projeto de gerenciamento de tarefas desenvolvido para o Bootcamp II.

## Como executar com Docker

**Como construir a imagem:**
`docker build -t tasktracker-image .`

**Como rodar o container em modo isolado:**
`docker run -it tasktracker-image`

**Como rodar via orquestração (Recomendado):**
`docker compose run tasktracker-app`