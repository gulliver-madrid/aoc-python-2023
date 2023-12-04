from src.utils import *
from .a import day_number

# Part 2


def solve(lines: Lines) -> int:
    potencias: list[int] = []
    for line in lines:
        # print(line)
        _, conjuntos_str = line.split(":")
        conjuntos2 = (s.strip() for s in conjuntos_str.split(";"))
        #  nuevo juego
        cubos = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for conj in conjuntos2:
            items = list(s.strip() for s in conj.split(","))
            assert len(items) <= 3
            for item in items:
                n_str, color = item.split(" ")
                n = int(n_str)

                if n > cubos[color]:
                    cubos[color] = n

        potencia = cubos["red"] * cubos["blue"] * cubos["green"]
        potencias.append(potencia)

    return sum(potencias)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
