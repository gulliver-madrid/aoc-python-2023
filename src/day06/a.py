from src.utils import *


day_number = get_day_number(__file__)


def parse(line: str) -> list[int]:
    return [int(s) for s in line.split(":")[1].split(" ") if s]


def solve(lines: Lines) -> int:
    times = parse(lines[0])
    distances = parse(lines[1])
    total = 1
    for t, d in zip(times, distances):
        count = 0
        for t_hold in range(t + 1):
            v = t_hold
            t_run = t - t_hold
            dist = t_run * v
            if dist > d:
                count += 1
        total *= count

    return total


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
