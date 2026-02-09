# Desafio Técnico — Refatoração de Processador de Transações

Abaixo temos um sistema que processa transações bancárias: **PIX, TED e boletos**.

O código atual funciona, porém está **acoplado e difícil de expandir**.  
Sua missão é refatorar essa classe para torná-la mais **modular, extensível e fácil de manter**.

Você pode alterar a estrutura como quiser — criar classes, interfaces, DTOs, patterns, etc.

O foco é **design e boas práticas**, não regras reais de banco.

## Como rodar o projeto

### Usando uv

```json
uv sync
uv run fastapi dev
```

### Usando pip
```json
pip install -r requirements.txt
fastapi dev
```

## Requisitos da Refatoração

Sua solução deve tornar o código:

- Mais **modular**
- Mais **extensível** para novos tipos de transação
- Mais **fácil de manter**
- Mais **fácil de testar**
- Mais **fácil de entender e usar**

## Exemplos de Payload do Swagger

### PIX
```json
{
  "transaction_type": "pix",
  "payload": {
    "pix_key": "123",
    "amount": 10.0,
    "description": "maistodos"
  }
}
```

### TED
```json
{
  "transaction_type": "ted",
  "payload": {
    "bank_code": "123",
    "agency": "123",
    "account_number": "123",
    "amount": 10.0
  }
}
```

### Boleto
```json
{
  "transaction_type": "boleto",
  "payload": {
    "payer_name": "John Doe",
    "amount": 10.0
  }
}
```