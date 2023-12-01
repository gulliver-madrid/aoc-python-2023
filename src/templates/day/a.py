import functools
import itertools
from pprint import pprint
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from pathlib import Path
import re
from src.utils import *
from string import ascii_lowercase, ascii_uppercase
from typing import Sequence, Final, NewType


day_number = get_day_number(__file__)


def solve(lines: Lines) -> int:
    for i, line in enumerate(lines):
        print(f"{i=}")
        print(line)
    print(f"Hay {len(lines)} lines")
    solution = 0
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
