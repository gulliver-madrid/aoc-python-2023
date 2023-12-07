from collections import Counter
import math
from typing import Callable, Mapping
from src.utils import *


day_number = get_day_number(__file__)

letter_cards = "AKQJT"

letter_cards_value = (14, 13, 12, 11, 10)
letters_to_value = dict(zip(letter_cards, letter_cards_value))

CardValues = tuple[int, int, int, int, int]
TypeValue = tuple[int, ...]
Score = tuple[TypeValue, CardValues]


def hand_type_score(hand: str) -> TypeValue:
    assert len(hand) == 5
    score = tuple(reversed(sorted(Counter(hand).values())))
    assert len(score) <= 5
    return score


def cards_value_score(hand: str, mapping: Mapping[str, int]) -> CardValues:
    assert len(hand) == 5
    values = tuple(mapping.get(card) or int(card) for card in hand)
    assert len(values) == 5
    return values


def get_score(hand: str) -> Score:
    assert len(hand) == 5
    return (hand_type_score(hand), cards_value_score(hand, letters_to_value))


def solve_with_score_func(lines: Lines, get_score_fun: Callable[[str], Score]) -> int:
    splitted = map(str.split, lines)
    score_bid_pairs = (
        (get_score_fun(hand), int(bid_str)) for hand, bid_str in splitted
    )
    sorted_pairs = sorted(score_bid_pairs, key=lambda x: x[0])
    rank_bid_pairs = ((i + 1, bid) for i, (_, bid) in enumerate(sorted_pairs))
    return sum(map(math.prod, rank_bid_pairs))


def solve(lines: Lines) -> int:
    return solve_with_score_func(lines, get_score)


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
