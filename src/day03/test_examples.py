import pytest
from src.utils import *

from . import a, b

given_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_a() -> None:
    expected = 4361
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_a"
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 467835
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_b"
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected
