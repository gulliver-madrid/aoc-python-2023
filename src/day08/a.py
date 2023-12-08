from typing import NewType
from src.utils import *


day_number = get_day_number(__file__)

Node = NewType("Node", str)

directions = "LR"


def parse_nodes(lines: Lines) -> dict[Node, tuple[Node, Node]]:
    nodes: dict[Node, tuple[Node, Node]] = {}
    for line in lines:
        nodo_str, neighbours_str = line.split(" = (")
        left = neighbours_str[:3]
        right = neighbours_str[5:8]
        nodes[Node(nodo_str)] = Node(left), Node(right)
    assert nodes
    return nodes


def solve(lines: Lines) -> int:
    nodes = parse_nodes(lines[2:])
    current = Node("AAA")
    steps = 0
    while current != "ZZZ":
        for command in lines[0]:
            steps += 1
            neighbours = nodes[current]
            next_node = neighbours[directions.index(command)]
            current = next_node
            if current == "ZZZ":
                break

    return steps


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
