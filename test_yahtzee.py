from yahtzee import *
import pytest


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test__roll__returns_correct_number_of_dice(n):
    assert len(roll(n)) == n


def test__roll__returns_dice_with_correct_values():
    for die in roll(5):
        assert die in range(1, 7)


@pytest.mark.parametrize("dice, keep, valid", [])
def test__keep__is_valid(dice, keep, valid):
    assert is_valid_to_keep(dice, keep) is valid


@pytest.mark.parametrize("dice, expected", [])
def test__score__ones(dice, expected):
    assert score_ones(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__twos(dice, expected):
    assert score_twos(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__threes(dice, expected):
    assert score_threes(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__fours(dice, expected):
    assert score_fours(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__fives(dice, expected):
    assert score_fives(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__sixes(dice, expected):
    assert score_sixes(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__3_of_a_kind(dice, expected):
    assert score_3_of_a_kind(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__4_of_a_kind(dice, expected):
    assert score_4_of_a_kind(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__small_straight(dice, expected):
    assert score_small_straight(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__large_straight(dice, expected):
    assert score_large_straight(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__full_house(dice, expected):
    assert score_full_house(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__chance(dice, expected):
    assert score_chance(dice) == expected


@pytest.mark.parametrize("dice, expected", [])
def test__score__yahtzee(dice, expected):
    assert score_yahtzee(dice) == expected
