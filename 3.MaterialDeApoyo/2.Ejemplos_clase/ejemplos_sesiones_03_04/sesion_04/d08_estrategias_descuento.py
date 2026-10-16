"""Guion S4, diapositiva 8: nuevas estrategias sin modificar el consumidor."""
from abc import ABC, abstractmethod
from typing import override


class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular(self, total: float) -> float:
        raise NotImplementedError


class DescuentoVIP(EstrategiaDescuento):
    @override
    def calcular(self, total: float) -> float:
        return total * 0.80


class DescuentoEmpleado(EstrategiaDescuento):
    @override
    def calcular(self, total: float) -> float:
        return total * 0.70


class DescuentoAgencia(EstrategiaDescuento):
    @override
    def calcular(self, total: float) -> float:
        return total * 0.85


class DescuentoMayorista(EstrategiaDescuento):
    @override
    def calcular(self, total: float) -> float:
        return total * 0.90


def cobrar(total: float, estrategia: EstrategiaDescuento) -> float:
    return round(estrategia.calcular(total), 2)


def main() -> None:
    estrategias: list[EstrategiaDescuento] = [
        DescuentoVIP(), DescuentoEmpleado(), DescuentoAgencia(), DescuentoMayorista()]
    for estrategia in estrategias:
        print(type(estrategia).__name__, cobrar(100.0, estrategia))
    # La composición cambia al elegir estrategias. cobrar permanece igual.


if __name__ == '__main__':
    main()
