########################################
# Score categories
########################################
def score_ones(dice: list[int]) -> int:
    """Score sum of all dice of a given value 1.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_twos(dice: list[int]) -> int:
    """Score sum of all dice of a given value 2.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_threes(dice: list[int]) -> int:
    """Score sum of all dice of a given value 3.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_fours(dice: list[int]) -> int:
    """Score sum of all dice of a given value 4.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_fives(dice: list[int]) -> int:
    """Score sum of all dice of a given value 5.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_sixes(dice: list[int]) -> int:
    """Score sum of all dice of a given value 6.

    Only the dice of the value are counted. The rest are ignored.
    """
    pass


def score_3_of_a_kind(dice: list) -> int:
    """Score sum of all dice if at least 3 die with a given value."""
    pass


def score_4_of_a_kind(dice: list) -> int:
    """Score sum of all dice if at least 4 die with a given value."""
    pass


def score_small_straight(dice: list[int]) -> int:
    """Score 30 if there is a straight of 4 dice."""
    pass


def score_large_straight(dice: list[int]) -> int:
    """Score 40 if there is a straight of 5 dice."""
    pass


def score_full_house(dice: list[int]) -> int:
    """Score 25 if there is a pair and a three of a kind.

    Allow for 5 of a kind to count as a pair and a three of a kind.
    """
    pass


def score_chance(dice: list[int]) -> int:
    """Score sum of all dice."""
    pass


def score_yahtzee(dice: list[int]) -> int:
    """Score 50 if all dice are the same."""
    pass


########################################
# Game Logic
########################################
def roll(n: int) -> list[int]:
    """Rolls n dice and returns the result in a list."""
    pass


def is_valid_to_keep(dice: list[int], keep: list[int]) -> bool:
    """Checks if the dice to keep are valid."""
    pass


def prompt_dice_to_keep(dice: list[int]) -> list[int]:
    """Prompts the user to keep dice and returns the result in a list."""
    pass


def prompt_category_to_score(scores: dict) -> str:
    pass


def show_scores(scores: dict):
    pass


def main():
    scores = {
        "Ones": {"score": 0, "used": False, "func": score_ones},
        "Twos": {"score": 0, "used": False, "func": score_twos},
        "Threes": {"score": 0, "used": False, "func": score_threes},
        "Fours": {"score": 0, "used": False, "func": score_fours},
        "Fives": {"score": 0, "used": False, "func": score_fives},
        "Sixes": {"score": 0, "used": False, "func": score_sixes},
        "Three of a Kind": {"score": 0, "used": False, "func": score_3_of_a_kind},
        "Four of a Kind": {"score": 0, "used": False, "func": score_4_of_a_kind},
        "Small Straight": {"score": 0, "used": False, "func": score_small_straight},
        "Large Straight": {"score": 0, "used": False, "func": score_large_straight},
        "Full House": {"score": 0, "used": False, "func": score_full_house},
        "Chance": {"score": 0, "used": False, "func": score_chance},
        "Yahtzee": {"score": 0, "used": False, "func": score_yahtzee},
    }


if __name__ == "__main__":
    main()
