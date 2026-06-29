# llm-cli

Lightweight terminal CLI for chatting with OpenAI-compatible LLMs. Streaming output, slash commands, token usage display.

## Setup

```bash
cp .env.example .env
# add your OPENAI_API_KEY to .env

uv sync
uv run main.py
```

## My Recommended VSCode Extensions

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

[Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

[Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Commands

| Command | Description |
|---|---|
| `/help` | Show available commands |
| `/model <name>` | Switch model |
| `/exit` | Quit |
