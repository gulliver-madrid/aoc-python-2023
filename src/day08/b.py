from itertools import count
import math
from collections import Counter
from typing import NewType
from src.utils import *
from .a import Node, day_number, directions, parse_nodes

# Part 2
Cursor = NewType("Cursor", int)


def get_divisors(value: int) -> Counter[int]:
    divisors: Counter[int] = Counter()
    checked: list[int] = []
    candidates = count(2)
    while value != 1:
        candidate = next(candidates)
        if any(candidate % num == 0 for num in checked):
            continue
        # podria haber una potencia
        while value % candidate == 0:
            divisors[candidate] += 1
            value //= candidate
            if value == 1:
                break
        checked.append(candidate)
    return divisors


def solve(lines: Lines) -> int:
    nodes = parse_nodes(lines[2:])
    assert nodes
    current_nodes: list[Node] = [nodo for nodo in nodes if nodo.endswith("A")]
    first_occurrences: dict[Cursor, tuple[Node, int]] = {}
    frequencies: dict[Cursor, int] = {}
    cursors = [Cursor(i) for i in range(len(current_nodes))]
    steps = 0

    while len(frequencies) < len(current_nodes):
        for command in lines[0]:
            steps += 1
            # movemos cada cursor
            for cursor in cursors:
                current = current_nodes[cursor]
                neighbours = nodes[current]
                next_node = neighbours[directions.index(command)]
                current_nodes[cursor] = next_node
                if not current.endswith("Z"):
                    continue
                # acaba en z
                if cursor not in first_occurrences:
                    # guarda la primera aparicion
                    first_occurrences[cursor] = (next_node, steps)
                    continue
                # ya estaba registrada la inicial
                target, steps_at_first_occurrence = first_occurrences[cursor]
                assert next_node == target
                steps_since_first_occurrence = steps - steps_at_first_occurrence
                if cursor not in frequencies:
                    frequencies[cursor] = steps_since_first_occurrence
                else:
                    assert steps_since_first_occurrence % frequencies[cursor] == 0

            if len(frequencies) == len(current_nodes):
                break

    # obtenemos el minimo comun multiplo
    divisors: Counter[int] = Counter()
    for freq in frequencies.values():
        divisors |= get_divisors(freq)
    solution = math.prod(div**pot for div, pot in divisors.items())
    assert isinstance(solution, int)
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
