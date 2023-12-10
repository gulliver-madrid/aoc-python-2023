from collections import deque
from typing import Sequence
from src.utils import *


day_number = get_day_number(__file__)


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

tipos_tuberias = {
    "|": set("NS"),
    "-": set("WE"),
    "L": set("NE"),
    "J": set("NW"),
    "7": set("SW"),
    "F": set("SE"),
    ".": set(""),
    "S": set("O"),
}


Node = tuple[int, int]


def get_tipo_start(pos: Node, lines: Sequence[str], line: str) -> set[str]:
    x, y = pos
    tipo: set[str] = set()
    if x > 0 and line[x - 1] in "-LF":
        tipo.add("W")
    if x < len(line) - 1 and line[x + 1] in "-J7":
        tipo.add("E")
    if y > 0 and lines[y - 1][x] in "|7F":
        tipo.add("N")
    if (y < len(lines) - 1) and lines[y + 1][x] in "|JL":
        tipo.add("S")
    assert tipo
    assert len(tipo) == 2
    return tipo


def get_neighbours(
    node: Node, tipo: set[str], lines: Lines, line: str
) -> tuple[Node, Node] | None:
    x, y = node
    neighbours_: list[Node] = []
    if "N" in tipo and y > 0:
        neighbours_.append((x, y - 1))
    if "S" in tipo and y < len(lines) - 1:
        neighbours_.append((x, y + 1))

    if "W" in tipo and x > 0:
        neighbours_.append((x - 1, y))
    if "E" in tipo and x < len(line) - 1:
        neighbours_.append((x + 1, y))

    if neighbours_:
        tup = tuple(neighbours_)
        if len(tup) == 2:
            assert len(tup) == 2
            return tup
    return None


def solve(lines: Lines) -> int:
    nodes: dict[Node, tuple[Node, Node]] = {}
    start: Node | None = None
    line = ""
    for y, line in enumerate(lines):
        assert line
        for x, char_ in enumerate(line):
            tipo: set[str] = tipos_tuberias[char_]
            node = (x, y)

            if "O" in tipo:
                tipo = get_tipo_start(node, lines, line)
                start = node
            neighbours = get_neighbours(node, tipo, lines, line)
            if neighbours:
                nodes[node] = neighbours

    visited: set[Node] = set()
    distances: dict[Node, int] = {}
    assert start

    distances[start] = 0
    to_visit: deque[Node] = deque([start])
    while to_visit:
        current = to_visit.popleft()
        neighbours = nodes.get(current)
        visited.add(start)
        current_distance = distances[current]
        assert neighbours
        a, b = neighbours
        for neighbour in (a, b):
            if neighbour in visited:
                continue
            x, y = neighbour
            assert 0 <= x < len(line)
            assert 0 <= y < len(lines)
            visited.add(neighbour)
            distances[neighbour] = current_distance + 1
            to_visit.append(neighbour)
    return max(distances.values())


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
