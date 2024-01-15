from random import randint
from collections import Counter
from functools import partial


########################################
# Score categories
########################################
def score_value(dice: list[int], value: int) -> int:
    """Score sum of all dice of a given value.

    Only the dice of the value are counted. The rest are ignored.
    """
    return sum([d for d in dice if d == value])


score_ones = partial(score_value, value=1)
score_twos = partial(score_value, value=2)
score_threes = partial(score_value, value=3)
score_fours = partial(score_value, value=4)
score_fives = partial(score_value, value=5)
score_sixes = partial(score_value, value=6)


def score_n_of_kind(dice: list, n: int) -> int:
    """Score sum of all dice least n die with a given value."""
    counts = Counter(dice)
    if max(counts.values()) >= n:
        return sum(dice)
    return 0


score_3_of_a_kind = partial(score_n_of_kind, n=3)
score_4_of_a_kind = partial(score_n_of_kind, n=4)


def score_small_straight(dice: list[int]) -> int:
    """Score 30 if there is a straight of 4 dice."""
    possible_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    for straight in possible_straights:
        if all(d in dice for d in straight):
            return 30
    return 0


def score_large_straight(dice: list[int]) -> int:
    """Score 40 if there is a straight of 5 dice."""
    possible_straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    for straight in possible_straights:
        if all(d in dice for d in straight):
            return 40
    return 0


def score_full_house(dice: list[int]) -> int:
    """Score 25 if there is a pair and a three of a kind.

    Allow for 5 of a kind to count as a pair and a three of a kind.
    """
    counts = Counter(dice)
    print(counts)
    if len(counts) == 2 and 2 in counts.values():
        return 25
    if len(counts) == 1:
        return 25
    return 0


def score_chance(dice: list[int]) -> int:
    """Score sum of all dice."""
    return sum(dice)


def score_yahtzee(dice: list[int]) -> int:
    """Score 50 if all dice are the same."""
    return 50 if len(set(dice)) == 1 else 0


########################################
# Game Logic
########################################
def roll(n: int) -> list[int]:
    """Rolls n dice and returns the result in a list."""
    return [randint(1, 6) for _ in range(n)]


def is_valid_to_keep(dice: list[int], keep: list[int]) -> bool:
    """Checks if the dice to keep are valid."""
    _dice = dice.copy()
    try:
        for d in keep:
            _dice.remove(d)
    except ValueError:
        return False

    return True


def prompt_dice_to_keep(dice: list[int]) -> list[int]:
    """Prompts the user to keep dice and returns the result in a list."""
    print("Your Dice:", ", ".join([str(d) for d in sorted(dice)]))
    while True:
        keep = input("Dice to keep (values): ")
        keep = [int(d) for d in keep if d.isdigit()]
        if is_valid_to_keep(dice, keep):
            return keep
        else:
            print("Invalid dice to keep!")


def prompt_category_to_score(scores: dict) -> str:
    selection = 0
    valid = []
    print("Score dice as:")
    for i, (k, v) in enumerate(scores.items(), 1):
        if not v["used"]:
            valid.append(i)
            print(f"> {i}. {k}")
    while selection not in valid:
        selection = int(input("Selection: "))

    return list(scores.keys())[selection - 1]


def show_scores(scores: dict):
    print("Scoreboard:")
    chars = max([len(k) for k in scores.keys()]) + 2
    for k, v in scores.items():
        print(f"{k:.<{chars}} {v['score']}")

    print(f"{'TOTAL':_<{chars}} {sum([v['score'] for v in scores.values()])}")


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

    while any(v["used"] == False for v in scores.values()):
        dice = roll(5)
        for _ in range(2):
            dice = prompt_dice_to_keep(dice)
            if len(dice) == 5:
                break
            else:
                dice += roll(5 - len(dice))

        print("Final Dice:", ", ".join([str(d) for d in sorted(dice)]))

        category = prompt_category_to_score(scores)
        scores[category]["score"] = scores[category]["func"](dice)
        show_scores(scores)


if __name__ == "__main__":
    main()
