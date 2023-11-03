import pytest
from mastermind_backend import MastermindGame

@pytest.fixture
def game():
    return MastermindGame()

def test_generate_secret_code(game):
    secret_code = game.generate_secret_code()
    assert len(secret_code) == 4
    assert all(color in "RGBYOP" for color in secret_code)

def test_check_guess_correct(game):
    game.secret_code = ["R", "G", "B", "Y"]
    feedback = game.check_guess("RGBY")
    assert feedback == ["R", "R", "R", "R"]

def test_check_guess_wrong(game):
    game.secret_code = ["R", "G", "B", "Y"]
    feedback = game.check_guess("OOPY")
    assert feedback == ["W", "W", " ", " "]

def test_check_guess_partial(game):
    game.secret_code = ["R", "G", "B", "Y"]
    feedback = game.check_guess("GROB")
    assert feedback == ["W", "W", "W", "W"]

def test_is_game_over_correct(game):
    game.secret_code = ["R", "G", "B", "Y"]
    assert game.is_game_over("RGBY")

def test_is_game_over_wrong(game):
    game.secret_code = ["R", "G", "B", "Y"]
    assert not game.is_game_over("OOPY")

def test_get_secret_code(game):
    game.secret_code = ["R", "G", "B", "Y"]
    assert game.get_secret_code() == ["R", "G", "B", "Y"]
