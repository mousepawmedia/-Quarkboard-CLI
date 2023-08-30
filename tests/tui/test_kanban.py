from ward import test
from quarkboard.tui import kanban


@test("test empty board has correct columns")
def _():
    board = kanban.build_board()
    headers = [col.header for col in board.columns]
    for header, expected in zip(headers, kanban.COLUMNS):
        assert header == expected


@test("test board has values")
def _():
    board = kanban.load_board()
    for column in board.columns:
        assert len(column._cells) > 0
