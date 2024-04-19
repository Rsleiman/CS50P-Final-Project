import pytest
from project import Card, CardGame

game = CardGame(start_game = False) # Allows me to create an instance of CardGame without starting the game for testing purposes
def test_rank_to_num():
    assert game.rank_to_num(rank = "king") == 13
    assert game.rank_to_num(rank = "nine") == 9
    assert game.rank_to_num(rank = "ace") == 14


def test__suit_setter():
    card = Card("s", "a")
    assert card.suit== "spade"
    card = Card("SPADE", "a")

    card = Card("sPADES", "a")

    with pytest.raises(Exception):
        card = Card("shovel", "a")




def test__rank_setter():
    card = Card("s", "a")
    assert card.rank == "ace"

    card = Card("s", "ACe")
    assert card.rank == "ace"

    card = Card("s", "A")
    assert card.rank == "ace"

    with pytest.raises(Exception):
        card = Card("s", "aced")
