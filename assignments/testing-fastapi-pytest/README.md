# 📘 Assignment: Testing FastAPI Endpoints with Pytest

## 🎯 Objective

Aprender a validar endpoints de uma API FastAPI com Pytest, cobrindo cenarios de sucesso e erro para aumentar a confiabilidade da aplicacao.

## 📝 Tasks

### 🛠️ Set Up API Test Environment

#### Descrição
Prepare o ambiente de testes e configure um cliente de teste para chamar os endpoints da API.

#### Requisitos
O programa concluído deve:

- Importar `TestClient` de FastAPI e conectar ao app definido em `starter-code.py`.
- Criar um teste para `GET /health` validando status code `200`.
- Validar que a resposta de `GET /health` possui o JSON esperado.

### 🛠️ Test Core CRUD Flows

#### Descrição
Escreva testes para os fluxos principais de cadastro e listagem de itens.

#### Requisitos
O programa concluído deve:

- Criar um teste para `POST /items` com payload valido.
- Confirmar que `GET /items` retorna o item criado.
- Validar status code e campos principais da resposta (`id`, `name`, `price`).

### 🛠️ Test Error Cases and Validation

#### Descrição
Adicione testes para garantir que a API responde corretamente em casos invalidos.

#### Requisitos
O programa concluído deve:

- Testar `GET /items/{item_id}` para item inexistente e validar `404`.
- Testar `DELETE /items/{item_id}` para item inexistente e validar `404`.
- Testar `POST /items` com payload invalido e validar erro de validacao (`422`).
