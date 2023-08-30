from ward import test
from quarkboard.data.tasks import fetch


@test("test fetching cards")
def _():
    cards = fetch()
    assert len(cards) > 0
