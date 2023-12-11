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


def get_directions(s: str) -> set[Direction]:
    return set(directions[char] for char in s)


tipos_tuberias = {
    "|": get_directions("NS"),
    "-": get_directions("WE"),
    "L": get_directions("NE"),
    "J": get_directions("NW"),
    "7": get_directions("SW"),
    "F": get_directions("SE"),
}


Node = tuple[int, int]


def get_tipo_start(pos: Node, lines: Sequence[str], line: str) -> set[Direction]:
    x, y = pos
    tipo: set[Direction] = set()
    if x > 0 and line[x - 1] in "-LF":
        tipo.add(Direction.W)
    if x < len(line) - 1 and line[x + 1] in "-J7":
        tipo.add(Direction.E)
    if y > 0 and lines[y - 1][x] in "|7F":
        tipo.add(Direction.N)
    if (y < len(lines) - 1) and lines[y + 1][x] in "|JL":
        tipo.add(Direction.S)
    assert tipo
    assert len(tipo) == 2
    return tipo


def get_neighbours(
    node: Node, tipo: set[Direction], dimensions: tuple[int, int]
) -> tuple[Node, Node] | None:
    x, y = node
    w, h = dimensions
    neighbours: list[Node] = []
    if Direction.N in tipo and y > 0:
        neighbours.append((x, y - 1))
    if Direction.S in tipo and y < h - 1:
        neighbours.append((x, y + 1))
    if Direction.W in tipo and x > 0:
        neighbours.append((x - 1, y))
    if Direction.E in tipo and x < w - 1:
        neighbours.append((x + 1, y))

    if neighbours:
        tup = tuple(neighbours)
        if len(tup) == 2:
            assert len(tup) == 2
            return tup
    return None


def solve(lines: Lines) -> int:
    nodes: dict[Node, tuple[Node, Node]] = {}
    start: Node | None = None
    dimensions = (len(lines[0]), len(lines))

    line = ""
    for y, line in enumerate(lines):
        assert line
        for x, char in enumerate(line):
            node = (x, y)
            tipo: set[Direction] | None = None
            if "S" in char:
                tipo = get_tipo_start(node, lines, line)
                start = node
            else:
                tipo = tipos_tuberias.get(char)

            if not tipo:
                continue

            neighbours = get_neighbours(node, tipo, dimensions)
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
