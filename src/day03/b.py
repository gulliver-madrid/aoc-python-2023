from functools import partial, reduce
import math
import operator
from pprint import pprint
from typing import Iterator, Sequence
from src.utils import *
from .a import (
    NumberWithPositions,
    build_numbers,
    day_number,
    Pos,
    is_adjacent,
)

# Part 2


def get_star_positions(lines: Lines) -> Iterator[Pos]:
    return (
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "*"
    )


def get_numbers_adjacent_to_pos(
    numbers_wp: Sequence[NumberWithPositions], pos: Pos
) -> Iterator[int]:
    return (num.value for num in numbers_wp if is_adjacent(num, pos))


def are_exactly_two(seq: Sequence[object]) -> bool:
    return len(seq) == 2


def solve(lines: Lines) -> int:
    numbers = build_numbers(lines)
    get_adjacent_numbers = partial(get_numbers_adjacent_to_pos, numbers)
    return sum(
        g(get_star_positions(lines))
        .map(get_adjacent_numbers)
        .map(tuple)
        .filter(are_exactly_two)
        .map(math.prod)
    )


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
