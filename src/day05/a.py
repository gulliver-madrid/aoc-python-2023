from src.utils import *


day_number = get_day_number(__file__)
Mapa = tuple[int, int, int]
Mapas = list[Mapa]


def parse_first_line(line: str) -> list[int]:
    return [int(s) for s in line.split(":")[1].strip().split()]


def mapea(inicial: int, mapas: Mapas) -> int:
    for dest, src, length in mapas:
        if src <= inicial < src + length:
            offset = inicial - src
            return dest + offset
    return inicial


def parsear_mapas(lines: Lines) -> list[Mapas]:
    todos_mapas: list[Mapas] = []
    mapas: Mapas | None = None
    for line in list(lines[1:]) + [""]:
        if line:
            if line[0].isdigit():
                assert mapas is not None
                mapas.append(tuple_three(int(s) for s in line.split()))
        else:
            if mapas:
                todos_mapas.append(mapas)
            mapas = []
    return todos_mapas


def solve(lines: Lines) -> int:
    semillas = parse_first_line(lines[0])
    todos_mapas = parsear_mapas(lines)

    locs: list[int] = []

    for sem in semillas:
        val = sem
        for mapa in todos_mapas:
            val = mapea(val, mapa)
        locs.append(val)
    assert len(semillas) == len(locs)

    return min(locs)


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
