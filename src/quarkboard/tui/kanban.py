"""Kanban board TUI."""

import itertools

from rich.table import Table

from quarkboard.data.tasks import fetch

COLUMNS = [
    "Backlog",
    "[bold yellow]Next[/bold yellow]",
    "[bold green]Now[/bold green]",
    "[bold cyan]Done[/bold cyan]",
]


def build_board() -> Table:
    """Build an empty Kanban board."""
    board = Table(show_header=True)
    board.add_column("Backlog")
    board.add_column("[bold yellow]Next[/bold yellow]")
    board.add_column("[bold green]Now[/bold green]")
    board.add_column("[bold cyan]Done[/bold cyan]")
    return board


def load_board() -> Table:
    """Build a Kanban board and populate with data."""
    board = build_board()
    cards_backlog = fetch()
    cards_next = fetch()
    cards_now = fetch()
    cards_done = fetch()
    for row in itertools.zip_longest(cards_backlog, cards_next, cards_now, cards_done):
        board.add_row(*row)
    return board
