from src.utils import *
from .a import day_number, obtener_aciertos

# Part 2


def solve(lines: Lines) -> int:
    cards = [1 for _ in lines]
    card_matches = g(lines).map(obtener_aciertos).list()

    # procesar premios
    for i, quantity in enumerate(cards):
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
