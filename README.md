# Controle de Gastos

Aplicação de controle financeiro pessoal com integração à API pública de cotação do dólar.

## Deploy
Acesse online: https://controle-gastos-eh4n.onrender.com

## Funcionalidades
- Adicionar e listar gastos
- Consultar cotação do dólar em tempo real (AwesomeAPI)

## Como executar localmente
```bash
py -m pip install -r requirements.txt
py src/main.pypython app.py
```

## Como rodar os testes
```bash
py -m pytest
```

## API utilizada
https://economia.awesomeapi.com.br/json/last/USD-BRL