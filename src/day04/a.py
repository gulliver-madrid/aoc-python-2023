import re
from src.utils import *


day_number = get_day_number(__file__)


def extraer_numeros(s: str) -> set[int]:
    matches = re.finditer(r"\d+", s)
    return set(int(m.group()) for m in matches)


def obtener_aciertos(line: str) -> int:
    _, a = line.split(":")
    gan, mis = a.split("|")
    num_ganadores = extraer_numeros(gan)
    mis_numeros = extraer_numeros(mis)
    return len(num_ganadores & mis_numeros)


def solve(lines: Lines) -> int:
    todos_los_aciertos = (obtener_aciertos(line) for line in lines)
    return sum(2 ** (aciertos - 1) for aciertos in todos_los_aciertos if aciertos)


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
