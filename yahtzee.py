########################################
# Score categories
########################################
import random
from collections import Counter


def score_ones(dice: list[int]) -> int:
    """Score sum of all dice of a given value 1.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(1)


def score_twos(dice: list[int]) -> int:
    """Score sum of all dice of a given value 2.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(2) * 2
    pass


def score_threes(dice: list[int]) -> int:
    """Score sum of all dice of a given value 3.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(3) * 3
    pass


def score_fours(dice: list[int]) -> int:
    """Score sum of all dice of a given value 4.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(4) * 4


def score_fives(dice: list[int]) -> int:
    """Score sum of all dice of a given value 5.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(5) * 5


def score_sixes(dice: list[int]) -> int:
    """Score sum of all dice of a given value 6.

    Only the dice of the value are counted. The rest are ignored.
    """
    return dice.count(6) * 6


def score_3_of_a_kind(dice: list) -> int:
    """Score sum of all dice if at least 3 die with a given value."""
    for x in range(1, 7):
        if dice.count(x) >= 3:
            return sum(dice)
    return 0


def score_4_of_a_kind(dice: list) -> int:
    """Score sum of all dice if at least 4 die with a given value."""
    for x in range(1, 7):
        if dice.count(x) >= 4:
            return sum(dice)
    return 0


def score_small_straight(dice: list[int]) -> int:
    """Score 30 if there is a straight of 4 dice."""
    dice = sorted(dice)
    pass


def score_large_straight(dice: list[int]) -> int:
    """Score 40 if there is a straight of 5 dice."""
    dice = sorted(dice)
    min = dice[0]
    max = dice[-1]
    if (max - min) != 4:
        return 0
    return 40


def score_full_house(dice: list[int]) -> int:
    """Score 25 if there is a pair and a three of a kind.

    Allow for 5 of a kind to count as a pair and a three of a kind.
    """
    dice_counter = Counter(dice)
    if (2 in dice_counter.values() and 3 in dice_counter.values()) or (
        5 in dice_counter.values()
    ):
        return 25
    return 0


def score_chance(dice: list[int]) -> int:
    """Score sum of all dice."""
    return sum(dice)


def score_yahtzee(dice: list[int]) -> int:
    """Score 50 if all dice are the same."""
    if len(set(dice)) == 1:
        return 50
    return 0


########################################
# Game Logic
########################################
def roll(n: int) -> list[int]:
    """Rolls n dice and returns the result in a list."""
    return [random.randint(1, 6) for _ in range(n)]


def is_valid_to_keep(dice: list[int], keep: list[int]) -> bool:
    """Checks if the dice to keep are valid."""
    for x in keep:
        if x not in dice:
            return False
    return True


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

    while not all_scores_used(scores):
        print("Rolling 5 dice...")
        input("Press Enter to roll...")
        pass


def all_scores_used(scores: dict) -> bool:
    """Checks if all scores have been used."""
    for x in scores:
        if scores[x]["used"] == False:
            return False
    return True


if __name__ == "__main__":
    main()
