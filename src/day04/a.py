import re
from src.utils import *


day_number = get_day_number(__file__)


def extraer_numeros(s: str) -> set[int]:
    matches = re.finditer(r"\d+", s)
    return set(int(m.group()) for m in matches)


def obtener_aciertos(line: str) -> int:
    gan, mis = line.split(":")[1].split("|")
    num_ganadores = extraer_numeros(gan)
    mis_numeros = extraer_numeros(mis)
    return len(num_ganadores & mis_numeros)


# fmt: off
def solve(lines: Lines) -> int:
    return sum(g(lines)
        .map(obtener_aciertos)
        .filter(bool)
        .map(lambda x: 2 ** (x - 1))
    )
# fmt: on


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
