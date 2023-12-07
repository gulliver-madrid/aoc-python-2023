import pytest
from src.utils import *

from . import a, b

given_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_a() -> None:
    expected = 6440
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 5905
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected
