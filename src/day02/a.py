from src.utils import *


day_number = get_day_number(__file__)


def solve(lines: Lines) -> int:
    posibles: list[int] = []
    for line in lines:
        juego, conjuntos_str = line.split(":")
        conjuntos2 = (s.strip() for s in conjuntos_str.split(";"))
        imposible = False
        for conj in conjuntos2:
            start = {
                "red": 12,
                "green": 13,
                "blue": 14,
            }
            items = (s.strip() for s in conj.split(","))
            for item in items:
                n_str, color = item.split(" ")
                n = int(n_str)
                start[color] -= n
                if start[color] < 0:
                    imposible = True
                    break
            if imposible:
                break
        if imposible:
            continue
        _, id_str = juego.split(" ")
        posibles.append(int(id_str))

    return sum(posibles)


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
