import itertools
from typing import Sequence
from src.utils import *


day_number = get_day_number(__file__)

EMPTY = "."
GALAXY = "#"
Pos = tuple[int, int]


def encontrar_vacias(lines: Lines) -> tuple[list[int], set[int]]:
    filas_vacias: list[int] = []
    columnas_vacias: set[int] = set(range(len(lines[0])))

    for y, line in enumerate(lines):
        if set(line) == {EMPTY}:
            filas_vacias.append(y)
        columnas_vacias -= {x for x, char in enumerate(line) if char != EMPTY}
    return (filas_vacias, columnas_vacias)


def find_galaxies(lines: Sequence[Sequence[str]]) -> list[Pos]:
    galaxies: list[Pos] = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == GALAXY:
                galaxies.append((x, y))
    return galaxies


def solve(lines_: Lines) -> int:
    lines = list(lines_)
    filas_vacias, columnas_vacias = encontrar_vacias(lines)
    for y in reversed(filas_vacias):
        lines.insert(y, lines[y])

    galaxies: list[Pos] = []
    nuevas: list[list[str]] = []
    for y, line in enumerate(lines):
        row: list[str] = []
        for x, char in enumerate(line):
            if x in columnas_vacias:
                row.append(char)
            row.append(char)
        nuevas.append(row)

    galaxies = find_galaxies(nuevas)
    galaxy_quantity = len(galaxies)

    # ya expandido

    pares = list(itertools.combinations(range(galaxy_quantity), 2))

    distances = 0
    for a, b in pares:
        x, y = galaxies[a]
        xx, yy = galaxies[b]
        dist = abs(xx - x) + abs(yy - y)
        distances += dist

    return distances


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
