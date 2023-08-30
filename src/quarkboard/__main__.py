"""The Click interface for Quarkboard."""

import click
from rich.console import Console

from quarkboard.tui.kanban import load_board


@click.group()
def cli() -> None:
    """Quarkboard Task Manager CLI."""


@cli.command(name="list")
def list_tasks() -> None:
    """List all tasks."""
    console: Console = Console()
    board = load_board()
    console.print(board)
