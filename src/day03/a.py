from dataclasses import dataclass, field
import re
from typing import Sequence
from src.utils import *

day_number = get_day_number(__file__)

Pos = tuple[int, int]
END = "#"


@dataclass
class NumberWithPositions:
    value: int
    positions: list[Pos]


def adjacent_positions(pos: Pos) -> list[Pos]:
    x, y = pos
    return [
        (x - 1, y),
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ]


def encontrar_numeros_con_posiciones(line: str) -> list[tuple[int, int, int]]:
    # Buscar todas las ocurrencias de numeros en la linea
    coincidencias = re.finditer(r"\d+", line)
    resultados: list[tuple[int, int, int]] = []

    for match in coincidencias:
        numero = match.group()
        inicio = match.start()
        fin = match.end()
        resultados.append((int(numero), inicio, fin))

    return resultados


def build_numbers(lines: Lines) -> list[NumberWithPositions]:
    numbers_wp: list[NumberWithPositions] = []
    for y, line in enumerate(lines):
        numeros_con_posiciones = encontrar_numeros_con_posiciones(line)
        numbers_wp.extend(
            [
                NumberWithPositions(numero, [(x, y) for x in range(inicio, fin)])
                for numero, inicio, fin in numeros_con_posiciones
            ]
        )
    return numbers_wp


def get_symbol_positions(lines: Lines) -> list[Pos]:
    symbols_pos: list[Pos] = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbols_pos.append((x, y))
    return symbols_pos


def is_adjacent(number_wp: NumberWithPositions, position: Pos) -> bool:
    assert position not in number_wp.positions
    return any(pos in number_wp.positions for pos in adjacent_positions(position))


def is_adjacent_to_any(
    number_wp: NumberWithPositions, positions: Sequence[Pos]
) -> bool:
    return any(is_adjacent(number_wp, pos) for pos in positions)


def get_part_numbers(
    symbol_positions: Sequence[Pos], numbers_wp: Sequence[NumberWithPositions]
) -> list[int]:
    return [
        number_wp.value
        for number_wp in numbers_wp
        if is_adjacent_to_any(number_wp, symbol_positions)
    ]


def solve(lines: Lines) -> int:
    numbers_wp = build_numbers(lines)
    symbol_positions = get_symbol_positions(lines)
    part_numbers = get_part_numbers(symbol_positions, numbers_wp)
    return sum(part_numbers)


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
