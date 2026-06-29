from __future__ import annotations

from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory


@dataclass
class Appstate:
    """Class to hold the application state."""

    model: str = "gpt-5.4-nano"


class SlashCommandCompleter(Completer):
    def __init__(self, commands: list[str]) -> None:
        self.commands = commands

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor

        if not text.startswith("/"):
            return

        for command in self.commands:
            if command.startswith(text):
                yield Completion(
                    command,
                    start_position=-len(text),
                )


def main() -> None:
    """Main function to run the LLM CLI application."""

    # Initializers
    load_dotenv()

    client = OpenAI()

    completer = SlashCommandCompleter(["/exit", "/help", "/model"])

    session = PromptSession(history=InMemoryHistory(), completer=completer)

    state = Appstate()

    print("Welcome to LLM CLI - Type '/exit' to quit or /help for more commands.")

    # Main loop
    while True:
        print(f"Current model: {state.model}")
        user_input = session.prompt("> ")

        if user_input.strip().lower() == "/exit":
            print("Exiting LLM CLI. Goodbye!")
            break

        elif user_input.strip().lower() == "/help":
            print("Available commands:")
            print("/exit - Exit the application")
            print("/help - Show this help message")
            print("/model <model_name> - Change the model (e.g., /model gpt-5.4-nano)")
            continue

        usage = None

        stream = client.chat.completions.create(
            model=state.model,
            messages=[
                {"role": "user", "content": f"{user_input}"},
            ],
            stream=True,
            stream_options={"include_usage": True},
        )

        for chunk in stream:
            if chunk.choices:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    print(delta.content, end="", flush=True)

            if getattr(chunk, "usage", None) is not None:
                usage = chunk.usage
        print()  # newline at end
        print()

        if usage:
            print("prompt_tokens:", usage.prompt_tokens)
            print("completion_tokens:", usage.completion_tokens)
            print("total_tokens:", usage.total_tokens)

        print()


if __name__ == "__main__":
    main()
