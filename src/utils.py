from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import time
from typing import Iterable, Sequence, TypeVar
from .hack_python import G_List, G_Dict, g

Lines = Sequence[str]


def read_from_folder(src_path: str, filename: str) -> str:
    """src_path should be __file__"""
    with open(Path(src_path).parent / filename, "r") as file:
        return file.read()[:-1]  # Remove last line break (added by vscode)


def get_day_number(filepath: str) -> int:
    return int(Path(filepath).parts[-2][-2:])


def read_data_from_day(day: int, extra: str = "") -> Lines:
    assert day <= 99
    path = f"data/{day:0>2}{extra}.txt"
    try:
        return _read_data(path)
    except FileNotFoundError:
        print(f"{path} not found. Reading input.txt\n")
    return _read_data(f"data/input.txt")


def _read_data(path: str) -> Lines:
    with open(path, "r") as input_file:
        text = input_file.read()
    return text.splitlines()


def to_int(lines: Lines) -> list[int]:
    """Convert each line in a integer"""
    return [int(linea) for linea in lines]


@dataclass
class Example:
    lines: Lines
    expected: int | str


def print_solution(valor: int | str) -> None:
    print(f"Solution: {valor}")


def create_example(given_input: str, expected: int | str) -> Example:
    return Example(given_input.split("\n"), expected)


_T = TypeVar("_T")


def tuple_two(iterable: Iterable[_T]) -> tuple[_T, _T]:
    tup = tuple(iterable)
    assert len(tup) == 2
    return tup


def tuple_three(iterable: Iterable[_T]) -> tuple[_T, _T, _T]:
    tup = tuple(iterable)
    assert len(tup) == 3
    return tup


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # pyright: ignore
        print("Tiempo transcurrido:", time.time() - self.start)


class Direction(Enum):
    E = 0
    S = 1
    W = 2
    N = 3


directions = dict(E=Direction.E, S=Direction.S, W=Direction.W, N=Direction.N)

__all__ = (
    "G_List",
    "G_Dict",
    "g",
    "read_from_folder",
    "get_day_number",
    "read_data_from_day",
    "to_int",
    "Example",
    "print_solution",
    "create_example",
    "Lines",
    "tuple_two",
    "tuple_three",
    "Timer",
    "Direction",
    "directions",
)
