from collections import deque
from src.utils import *
from .a import Node, day_number, get_neighbours, get_tipo_start, tipos_tuberias

# Part 2


visualization = True


def solve(lines: Lines) -> int:
    nodes: dict[Node, tuple[Node, Node]] = {}
    start: Node | None = None
    dimensions = (len(lines[0]), len(lines))

    line = ""
    tipo_start: set[Direction] = set()
    for y, line in enumerate(lines):
        if visualization:
            print()
        assert line
        for x, char in enumerate(line):
            if visualization:
                print(char, end="")
            node = (x, y)
            tipo: set[Direction] | None = None
            if char == "S":
                start = node
                tipo = get_tipo_start(node, lines, line)
                tipo_start |= tipo
            else:
                tipo = tipos_tuberias.get(char)
            if not tipo:
                continue
            neighbours = get_neighbours(node, tipo, dimensions)
            if neighbours:
                nodes[node] = neighbours

    visited: set[Node] = set()
    assert start

    to_visit: deque[Node] = deque([start])
    while to_visit:
        current = to_visit.popleft()
        neighbours = nodes.get(current)
        visited.add(start)
        assert neighbours
        a, b = neighbours
        for neighbour in (a, b):
            if neighbour in visited:
                continue
            x, y = neighbour
            assert 0 <= x < len(line)
            assert 0 <= y < len(lines)
            visited.add(neighbour)
            to_visit.append(neighbour)

    node_path = frozenset(visited)
    inner_nodes: list[Node] = []
    foto: list[list[str]] = []
    for y in range(len(lines)):
        foto.append(["." for _ in range(len(lines[0]))])
        inside = False
        opened = ""
        for x in range(len(line)):
            if (x, y) in node_path:
                char = lines[y][x]
                # Replace S for their actual shape
                if char == "S":
                    assert len(tipo_start) == 2
                    char = next(k for k, v in tipos_tuberias.items() if tipo_start == v)
                    assert char

                if char == "|":
                    inside = not inside

                if char not in "LJ7F":
                    continue

                # it's a corner
                if not opened:
                    assert char in "LF"
                    opened = char
                else:
                    assert opened in "LF"
                    assert char in "J7"
                    if opened + char in ("L7", "FJ"):
                        inside = not inside
                    opened = ""
            else:
                if inside:
                    inner_nodes.append((x, y))
                if visualization:
                    foto[y][x] = "I" if inside else "O"
    if visualization:
        for row in foto:
            print("".join(row))
    return len(inner_nodes)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
