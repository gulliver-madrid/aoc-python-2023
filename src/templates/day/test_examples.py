import pytest
from src.utils import *

from . import a, b

given_input = """"""


def test_a() -> None:
    expected = 0
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_a"
    example = create_example(given_input, expected)
    result = a.solve(example.lines)
    assert result == example.expected


@pytest.mark.skip(reason="Not implemented")
def test_b() -> None:
    expected = 0
    assert given_input, "No hay un input de ejemplo"
    assert expected != 0, "Expected está definido como 0. Revisar su valor en test_b"
    example = create_example(given_input, expected)
    result = b.solve(example.lines)
    assert result == example.expected


@pytest.mark.skip(reason="Not implemented")
def test_func_int() -> None:
    result: int = a.func_int()  # type: ignore
    expected = 0
    assert result == expected


@pytest.mark.skip(reason="Not implemented")
def test_func_str() -> None:
    result: str = a.func_str()  # type: ignore
    expected = ""
    assert result == expected
