# Discord Account Details Bot

Este é um bot simples desenvolvido em Python utilizando a biblioteca `discord.py`. O bot fornece detalhes básicos da conta do utilizador e informações relacionadas ao IP público do servidor onde o bot está a correr.

---

## Funcionalidades

- Comando `!help`: Exibe uma lista de comandos disponíveis.
- Comando `!account`: Mostra uma embed com informações do utilizador (nome, ID, status, boost) e dados geográficos e financeiros associados ao IP público do bot, consultando a API pública [ipapi.co](https://ipapi.co/).

---

## Tecnologias e Bibliotecas Utilizadas

- Python 3.7+
- [discord.py](https://discordpy.readthedocs.io/en/stable/) (`discord.ext.commands`)
- Biblioteca padrão `urllib` para requisições HTTP
- `asyncio` para execução assíncrona

---

## Como usar

### Pré-requisitos

- Ter Python 3.7 ou superior instalado
- Criar um bot na [Discord Developer Portal](https://discord.com/developers/applications) e obter o token
- Instalar a biblioteca `discord.py`:

```bash
pip install -U discord.py
