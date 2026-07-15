"""Model registry: pricing and context-window info for available models."""

MODELS = {
    "gpt-5.6-luna": {
        "provider": "openai",
        "context_window": 1_050_000,
        "cost": {
            "input": 0.000001,
            "output": 0.000006,
        },
    },
    "gpt-5.6-terra": {
        "provider": "openai",
        "context_window": 1_050_000,
        "cost": {
            "input": 0.0000025,
            "output": 0.000015,
        },
    },
    "gpt-5.4-mini": {
        "provider": "openai",
        "context_window": 400_000,
        "cost": {
            "input": 0.00000075,
            "output": 0.0000045,
        },
    },
    "gpt-5.4-nano": {
        "provider": "openai",
        "context_window": 400_000,
        "cost": {
            "input": 0.0000002,
            "output": 0.00000125,
        },
    },
    "gpt-5.3-codex": {
        "provider": "openai",
        "context_window": 400_000,
        "cost": {
            "input": 0.00000175,
            "output": 0.000014,
        },
    },
}

DEFAULT_MODEL = "gpt-5.4-mini"
