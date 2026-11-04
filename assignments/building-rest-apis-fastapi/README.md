# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST básica com FastAPI, praticando criação de rotas, validação de dados e operações CRUD em memória.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Descrição
Crie a estrutura inicial da aplicação e implemente rotas simples para confirmar que o servidor está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI em `starter-code.py`.
- Implementar uma rota `GET /` que retorne uma mensagem de boas-vindas em JSON.
- Implementar uma rota `GET /health` que retorne o status da API.

### 🛠️ Build Item CRUD Endpoints

#### Descrição
Implemente endpoints para cadastrar, listar e consultar itens usando uma lista em memória.

#### Requisitos
O programa concluído deve:

- Criar um modelo `Item` com `id`, `name` e `price`.
- Implementar `POST /items` para adicionar um item.
- Implementar `GET /items` para listar todos os itens.
- Implementar `GET /items/{item_id}` para buscar um item por ID.
- Retornar erro `404` quando o item não existir.

### 🛠️ Add Update and Delete Operations

#### Descrição
Complete o ciclo CRUD com atualização e remoção de itens e respostas HTTP apropriadas.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /items/{item_id}` para atualizar `name` e `price`.
- Implementar `DELETE /items/{item_id}` para remover um item.
- Retornar erro `404` em update/delete quando o item não existir.
- Retornar mensagens JSON claras para sucesso e erro.
