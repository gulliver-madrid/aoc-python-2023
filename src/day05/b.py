from src.utils import *
from .a import Mapas, day_number, parse_first_line, parsear_mapas

# Part 2


def mapea_rango(entrada: range, mapas: Mapas) -> range:
    """Devuelve el rango de salida"""
    assert entrada

    for dest, src, length in mapas:
        src_range = range(src, src + length)
        if entrada.start in src_range:
            consumida = range(entrada.start, min(entrada.stop, src_range.stop))

            # cuanto desplaza los valores el mapa (puede ser negativo)
            offset = dest - src
            assert dest == src_range.start + offset
            assert (
                dest + length == src_range.stop + offset
            )  # maximo final del rango de salida del mapa

            # obtenemos el rango de salida
            salida = range(consumida.start + offset, consumida.stop + offset)
            assert salida
            return salida

    # no hay un mapa adecuado
    return entrada


def obtener_rangos(datos: list[int]) -> list[range]:
    rangos: list[range] = []
    while datos:
        a = datos.pop(0)
        b = datos.pop(0)
        rangos.append(range(a, a + b))
    return rangos


def solve(lines: Lines) -> int:
    datos_semillas = parse_first_line(lines[0])
    rangos = obtener_rangos(datos_semillas)
    todos_mapas = parsear_mapas(lines)

    rangos_actuales = rangos
    rangos_salida: list[range] = []

    for mapas in todos_mapas:
        for rango in rangos_actuales:
            end = rango.stop
            cursor = rango.start
            while cursor < end:
                rango_salida = mapea_rango(range(cursor, end), mapas)
                assert rango_salida
                rangos_salida.append(rango_salida)
                cursor += len(rango_salida)
            assert cursor == end
        rangos_actuales = rangos_salida
        rangos_salida = []

    assert rangos_actuales

    starts = [rango[0] for rango in rangos_actuales]

    return min(starts)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
