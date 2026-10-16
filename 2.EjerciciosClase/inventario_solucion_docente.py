"""Solución docente del ejercicio de cierre de inventario."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Movimiento:
    sku: str
    variacion: int


class Articulo:
    def __init__(self, sku: str, precio: float, existencias: int) -> None:
        self.sku = sku
        self.precio = precio
        self._existencias = existencias

    @property
    def existencias(self) -> int:
        return self._existencias

    @property
    def valor_en_almacen(self) -> float:
        return self.precio * self._existencias

    def aplicar_variacion(self, variacion: int) -> bool:
        nuevas_existencias = self._existencias + variacion
        if nuevas_existencias < 0:
            return False
        self._existencias = nuevas_existencias
        return True

    def __repr__(self) -> str:
        return f"Articulo(sku={self.sku!r}, existencias={self._existencias})"


def procesar_movimientos(
    inventario: dict[str, Articulo], movimientos: list[Movimiento]
) -> list[str]:
    incidencias: list[str] = []
    for movimiento in movimientos:
        articulo = inventario.get(movimiento.sku)
        if articulo is None:
            incidencias.append(f"{movimiento.sku}: SKU desconocido")
        elif not articulo.aplicar_variacion(movimiento.variacion):
            incidencias.append(f"{movimiento.sku}: existencias insuficientes")
    return incidencias


def skus_bajo_minimo(inventario: dict[str, Articulo], minimo: int) -> list[str]:
    return [
        sku for sku, articulo in inventario.items()
        if articulo.existencias <= minimo
    ]


def valor_por_sku(inventario: dict[str, Articulo]) -> dict[str, float]:
    return {sku: articulo.valor_en_almacen for sku, articulo in inventario.items()}


def main() -> None:
    inventario = {
        "A-10": Articulo("A-10", 12.50, 8),
        "B-20": Articulo("B-20", 4.00, 3),
        "C-30": Articulo("C-30", 9.50, 6),
    }
    movimientos = [
        Movimiento("A-10", -4),
        Movimiento("B-20", +5),
        Movimiento("C-30", -7),
        Movimiento("X-99", +2),
        Movimiento("A-10", +1),
    ]

    incidencias = procesar_movimientos(inventario, movimientos)
    existencias_finales = {
        sku: articulo.existencias for sku, articulo in inventario.items()
    }
    bajo_minimo = skus_bajo_minimo(inventario, 5)
    valores = valor_por_sku(inventario)

    print("Incidencias:", incidencias)
    print("Existencias finales:", existencias_finales)
    print("SKU con 5 existencias o menos:", bajo_minimo)
    print("Valor por SKU:", valores)

    assert incidencias == [
        "C-30: existencias insuficientes",
        "X-99: SKU desconocido",
    ]
    assert existencias_finales == {"A-10": 5, "B-20": 8, "C-30": 6}
    assert bajo_minimo == ["A-10"]
    assert valores == {"A-10": 62.5, "B-20": 32.0, "C-30": 57.0}


if __name__ == "__main__":
    main()
