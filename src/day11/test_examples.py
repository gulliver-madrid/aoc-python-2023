import pytest
from src.utils import *

from . import a, b

given_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_a() -> None:
    expected = 374
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 8410
    example = create_example(given_input, expected)
    result = b.solve(example.lines, expansion=100)
    assert result == example.expected


def test_b2() -> None:
    expected = 1030
    example = create_example(given_input, expected)
    result = b.solve(example.lines, expansion=10)
    assert result == example.expected
