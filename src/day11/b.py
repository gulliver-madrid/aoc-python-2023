import itertools
from src.utils import *
from .a import day_number, encontrar_vacias, find_galaxies

# Part 2
EXPANSION = 10**6


def solve(lines_: Lines, expansion: int = EXPANSION) -> int:
    lines = list(lines_)
    filas_vacias, columnas_vacias = encontrar_vacias(lines)

    # Crea equivalencias para el universo expandido
    equivalencias_x: list[int] = []
    equivalencias_y: list[int] = []
    for x in range(len(lines[0])):
        previa = equivalencias_x[-1] if x > 0 else -1
        if x in columnas_vacias:
            equivalencias_x.append(previa + expansion)
        else:
            equivalencias_x.append(previa + 1)
    for y in range(len(lines)):
        previa = equivalencias_y[-1] if y > 0 else -1
        if y in filas_vacias:
            equivalencias_y.append(previa + expansion)
        else:
            equivalencias_y.append(previa + 1)

    galaxies = find_galaxies(lines)
    galaxy_quantity = len(galaxies)
    pares = list(itertools.combinations(range(galaxy_quantity), 2))

    distances = 0
    for a, b in pares:
        x, y = galaxies[a]
        x = equivalencias_x[x]
        y = equivalencias_y[y]
        xx, yy = galaxies[b]
        xx = equivalencias_x[xx]
        yy = equivalencias_y[yy]
        dist = abs(xx - x) + abs(yy - y)
        distances += dist

    return distances


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
# 10885634 no es
