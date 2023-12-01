import functools
import itertools
from pprint import pprint
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from pathlib import Path
from typing import Sequence, Final, NewType
import re
from src.utils import *
from .a import day_number
from string import ascii_lowercase, ascii_uppercase

# Part 2


def solve(lines: Lines) -> int:
    for i, line in enumerate(lines):
        print(f"{i=}")
        print(line)
    print(f"Hay {len(lines)} lines")
    solution = 0
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
