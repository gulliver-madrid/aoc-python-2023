from src.utils import *


day_number = get_day_number(__file__)

Row = list[int]
Rows = list[Row]


def parse_lines(lines: Lines) -> Rows:
    seqs: Rows = []
    for line in lines:
        seqs.append([int(s) for s in line.split()])
    return seqs


def build_history_processes(seqs: Rows) -> list[Rows]:
    all_rows: list[Rows] = []
    for seq in seqs:
        rows: Rows = [seq]
        while not all(x == 0 for x in (rows[-1])):
            last = rows[-1]
            next_row: Row = []
            for i in range(len(last) - 1):
                next_row.append(last[i + 1] - last[i])
            rows.append(next_row)
        all_rows.append(rows)
    return all_rows


def solve(lines: Lines) -> int:
    seqs = parse_lines(lines)
    all_rows = build_history_processes(seqs)
    total = 0
    for rows in all_rows:
        for i in range(len(rows) - 1, 0, -1):
            rows[i - 1].append(rows[i - 1][-1] + rows[i][-1])
        total += rows[0][-1]
    return total


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
