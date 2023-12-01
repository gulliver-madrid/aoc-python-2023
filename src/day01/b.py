from src.utils import *
from .a import day_number

# Part 2

letters = "one, two, three, four, five, six, seven, eight, nine".split(", ")


def letter_to_int(letter: str) -> int:
    return letters.index(letter) + 1  # pyright: ignore


def get_first(line: str) -> int:
    first = None

    for i, char in enumerate(line):
        if char.isdigit():
            first = int(char)
            break
        found = False
        for let in letters:
            if line.startswith(let, i):
                first = letter_to_int(let)
                found = True
                break
        if found:
            break
    else:
        assert False, "No se encontró el primer dígito"
    assert first is not None
    return first


def get_last(line: str) -> int:
    last = None

    n = len(line)
    for i in range(n - 1, -1, -1):
        char = line[i]
        if char.isdigit():
            last = int(char)
            break

        found = False
        for let in letters:
            if line.endswith(let, 0, i + 1):
                last = letter_to_int(let)
                found = True
                break
        if found:
            break
    else:
        assert False, "No se encontró el último dígito"
    assert last is not None
    return last


def line_to_calibration(line: str) -> int:
    first = get_first(line)
    last = get_last(line)
    return first * 10 + last


def solve(lines: Lines) -> int:
    total = 0
    for line in lines:
        total += line_to_calibration(line)
    return total


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
