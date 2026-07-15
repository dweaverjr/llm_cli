"""Interactive REPL for chatting with an OpenAI-compatible LLM."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

from dotenv import load_dotenv
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory

from config import DEFAULT_MODEL, MODELS
from llm_client import LLMClient
from utils import calculate_cost, format_cost

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from prompt_toolkit.completion import CompleteEvent
    from prompt_toolkit.document import Document


SEPARATOR = "─" * 50

COMMANDS = ["/exit", "/help", "/model", "/max-tokens"]


@dataclass
class Appstate:
    """Class to hold the application state."""

    model: str = DEFAULT_MODEL
    max_tokens: int = 2000


class SlashCommandCompleter(Completer):
    """Autocomplete slash commands typed at the prompt."""

    def __init__(self, commands: list[str]) -> None:
        """Store the list of slash commands to offer as completions."""
        self.commands = commands

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        """Yield matching slash commands for the current input."""
        del complete_event
        text = document.text_before_cursor

        if not text.startswith("/"):
            return

        for command in self.commands:
            if command.startswith(text):
                yield Completion(
                    command,
                    start_position=-len(text),
                )


def print_help() -> None:
    """Print the list of available slash commands."""
    print("Available commands:")
    print("/exit - Exit the application")
    print("/help - Show this help message")
    print("/model - Choose a model from a numbered list")
    print(f"/model <name> - Change the model directly (choices: {', '.join(MODELS)})")
    print("/max-tokens <value> - Change the max output tokens")


def _cmd_exit(_arg: str, _state: Appstate) -> bool:
    """Handle the /exit command."""
    print("Exiting LLM CLI. Goodbye!")
    return False


def _cmd_help(_arg: str, _state: Appstate) -> bool:
    """Handle the /help command."""
    print_help()
    return True


def _cmd_model(arg: str, state: Appstate) -> bool:
    """Handle the /model command."""
    if arg:
        if arg in MODELS:
            state.model = arg
            print(f"Model set to: {arg}")
        else:
            print(f"Unknown model '{arg}'. Choices: {', '.join(MODELS)}")
        return True

    model_names = list(MODELS)
    print("Available models:")
    for i, model_name in enumerate(model_names, start=1):
        marker = "*" if model_name == state.model else " "
        print(f"  {marker} {i}. {model_name}")

    choice = input(f"Select a model [1-{len(model_names)}] (Enter to cancel): ").strip()
    if not choice:
        print("No change.")
    elif choice.isdigit() and 1 <= int(choice) <= len(model_names):
        state.model = model_names[int(choice) - 1]
        print(f"Model set to: {state.model}")
    else:
        print(f"Invalid selection '{choice}'.")
    return True


def _cmd_max_tokens(arg: str, state: Appstate) -> bool:
    """Handle the /max-tokens command."""
    try:
        state.max_tokens = int(arg)
        print(f"Max tokens set to: {state.max_tokens}")
    except ValueError:
        print("Usage: /max-tokens <int>")
    return True


COMMAND_HANDLERS: dict[str, Callable[[str, Appstate], bool]] = {
    "/exit": _cmd_exit,
    "/help": _cmd_help,
    "/model": _cmd_model,
    "/max-tokens": _cmd_max_tokens,
}


def handle_command(command: str, state: Appstate) -> bool:
    """Handle a slash command. Return False if the app should exit."""
    parts = command.strip().split(maxsplit=1)
    name = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""

    handler = COMMAND_HANDLERS.get(name)
    if handler is None:
        print(f"Unknown command: {name}. Type /help for a list of commands.")
        return True

    return handler(arg, state)


def main() -> None:
    """Run the LLM CLI application."""
    # Initializers
    load_dotenv()

    completer = SlashCommandCompleter(COMMANDS)

    session = PromptSession(history=InMemoryHistory(), completer=completer)

    state = Appstate()
    client = LLMClient(state.model)

    print("Welcome to LLM CLI - Type '/exit' to quit or /help for more commands.")

    # Main loop
    while True:
        print(f"Current model: {state.model}")
        user_input = session.prompt("> ").strip()

        if not user_input:
            continue

        if user_input.startswith("/"):
            if not handle_command(user_input, state):
                break
            continue

        client.model = state.model

        start = time.perf_counter()
        output_text = ""
        for token in client.stream(user_input, state.max_tokens):
            output_text += token
            print(token, end="", flush=True)
        print("\n")

        latency = time.perf_counter() - start
        usage = client.last_usage

        if usage:
            cost_config = MODELS[state.model]["cost"]
            cost = calculate_cost(
                usage.prompt_tokens,
                usage.completion_tokens,
                cost_config["input"],
                cost_config["output"],
            )
            print(SEPARATOR)
            print(f"Latency:       {latency:.2f}s")
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Output tokens: {usage.completion_tokens}")
            print(f"Total tokens:  {usage.total_tokens}")
            print(f"Cost:          {format_cost(cost)}")
            print(SEPARATOR)

        print()


if __name__ == "__main__":
    main()
