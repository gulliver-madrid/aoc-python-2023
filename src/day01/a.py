from src.utils import *


day_number = get_day_number(__file__)


def solve(lines: Lines) -> int:
    total = 0
    first = None
    last = None
    for line in lines:
        for char in line:
            if char.isdigit():
                first = char
                break
        else:
            assert False
        for char in reversed(line):
            if char.isdigit():
                last = char
                break
        else:
            assert False

        calibration = int(first + last)
        total += calibration

    return total


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
