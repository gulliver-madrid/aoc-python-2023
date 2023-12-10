import pytest
from src.utils import *

from . import a, b

given_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""


def test_a() -> None:
    expected = 4
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_a"
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


def test_b() -> None:
    expected = 4
    given_input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_b"
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected


def test_c() -> None:
    expected = 8
    given_input = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_b"
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected
