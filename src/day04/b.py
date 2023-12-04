from typing import NewType
from src.utils import *
from .a import day_number, obtener_aciertos

# Part 2

MatchesCount = NewType("MatchesCount", int)

Cards = list[int]
CardMatches = list[MatchesCount]


def calculate_initial_state(lines: Lines) -> tuple[Cards, CardMatches]:
    cards: Cards = []
    card_matches: CardMatches = []
    for line in lines:
        matches = obtener_aciertos(line)
        cards.append(1)
        card_matches.append(MatchesCount(matches))
    return cards, card_matches


def solve(lines: Lines) -> int:
    cards, card_matches = calculate_initial_state(lines)

    # procesar premios
    for i in range(len(cards)):
        quantity = cards[i]
        if quantity == 0:
            continue
        matches = card_matches[i]
        for offset in range(1, matches + 1):
            cards[i + offset] += quantity

    return sum(cards)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
