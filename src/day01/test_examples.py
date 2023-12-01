import pytest
from src.utils import *

from . import a, b

given_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

given_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_a() -> None:
    expected = 142
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 281
    example = create_example(given_input2, expected)
    res = b.solve(example.lines)
    assert res == example.expected
