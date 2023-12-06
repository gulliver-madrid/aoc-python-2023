from src.utils import *
from .a import day_number

# Part 2


def parse(line: str) -> int:
    return int(line.split(":")[1].replace(" ", ""))


def solve(lines: Lines) -> int:
    time = parse(lines[0])
    distance = parse(lines[1])

    count = 0
    for t_hold in range(time + 1):
        v = t_hold
        t_run = time - t_hold
        dist = t_run * v
        if dist <= distance:
            count += 1
        else:
            break
    from_start = count

    count = 0
    for t_hold in range(time, -1, -1):
        v = t_hold
        t_run = time - t_hold
        dist = t_run * v
        if dist <= distance:
            count += 1
        else:
            break
    from_end = count

    return time + 1 - from_start - from_end


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
