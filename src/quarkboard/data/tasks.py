"""Fetch tasks."""


def fetch() -> list[str]:
    """Fetch tasks."""
    # NOTE: This is written to create some temporary fake data. Replace with real fetching.
    # Likely we should change "str" to some sort of object representing each card.
    import random

    possibles = ["Frobinate", "Intertwine", "Scrutinize", "Broadcast", "Dismantle"]
    return random.sample(possibles, random.randint(1, 3))
