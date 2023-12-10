from collections import deque
from src.utils import *
from .a import Node, day_number, get_neighbours, get_tipo_start, tipos_tuberias

# Part 2


visualization = True


def solve(lines: Lines) -> int:
    nodes: dict[Node, tuple[Node, Node]] = {}
    start: Node | None = None

    line = ""
    tipo_start: set[str] = set()
    for y, line in enumerate(lines):
        if visualization:
            print()
        assert line
        for x, char_ in enumerate(line):
            if visualization:
                print(char_, end="")
            tipo: set[str] = tipos_tuberias[char_]
            node = (x, y)

            if tipo == {"O"}:
                tipo = get_tipo_start(node, lines, line)
                start = node
                tipo_start = set(tipo)
            neighbours = get_neighbours(node, tipo, lines, line)

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

    dentro: list[Node] = []
    foto: list[list[str]] = []
    for y in range(len(lines)):
        foto.append(["." for _ in range(len(lines[0]))])
        fuera = True
        is_open = ""
        for x in range(len(line)):
            if (x, y) in visited:
                char = lines[y][x]
                if char == "S":
                    char = ""
                    assert len(tipo_start) == 2
                    found = ""
                    for k, v in tipos_tuberias.items():
                        if tipo_start == v:
                            found = k
                            break
                    assert found
                    char = found
                if char in "|":
                    fuera = not fuera
                elif char in "LJ7F":
                    if not is_open:
                        is_open = char
                    else:
                        assert is_open in "LF", (is_open, (x, y))
                        assert char in "J7", (is_open, (x, y))
                        if is_open + char in ("L7", "FJ"):
                            fuera = not fuera
                        is_open = ""

            else:
                if not fuera:
                    dentro.append((x, y))
                if visualization:
                    if not fuera:
                        foto[y][x] = "I"
                    else:
                        foto[y][x] = "O"
    if visualization:
        for row in foto:
            print("".join(row))
    return len(dentro)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
