from src.utils import *
from .a import build_history_processes, day_number, parse_lines

# Part 2


def solve(lines: Lines) -> int:
    seqs = parse_lines(lines)
    all_rows = build_history_processes(seqs)
    total = 0
    for rows in all_rows:
        for i in range(len(rows) - 1, 0, -1):
            rows[i - 1].insert(0, rows[i - 1][0] - rows[i][0])
        total += rows[0][0]
    return total


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
