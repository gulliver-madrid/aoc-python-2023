import itertools
from typing import Final
from src.utils import *
from .a import (
    Score,
    cards_value_score,
    day_number,
    hand_type_score,
    solve_with_score_func,
)

# Part 2
JOKER: Final = "J"
available_cards: Final = "AKQJT98765432"

letter_cards: Final = "AKQJT"
letter_cards_value: Final = (14, 13, 12, 1, 10)
letters_to_value: Final = dict(zip(letter_cards, letter_cards_value))


def get_new_score(hand: str) -> Score:
    num_jokers = hand.count(JOKER)
    replacements = (
        iter(seq)
        for seq in itertools.combinations_with_replacement(available_cards, num_jokers)
    )
    max_type_score = max(
        hand_type_score("".join(next(seq) if char == JOKER else char for char in hand))
        for seq in replacements
    )
    return (max_type_score, cards_value_score(hand, letters_to_value))


def solve(lines: Lines) -> int:
    return solve_with_score_func(lines, get_new_score)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
