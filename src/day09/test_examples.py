import pytest
from src.utils import *

from . import a, b

given_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_a() -> None:
    expected = 114
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_a"
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 2
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_b"
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected
