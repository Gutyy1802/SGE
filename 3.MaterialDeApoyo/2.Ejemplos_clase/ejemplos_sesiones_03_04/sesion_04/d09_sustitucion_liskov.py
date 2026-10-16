"""Guion S4, diapositiva 9: firmas correctas no garantizan cumplir LSP."""
from typing import override


class Factura:
    def __init__(self, base: float) -> None:
        self.base: float = base

    def calcular_iva(self) -> float:
        """Contrato: devolver un importe no negativo para una base válida."""
        return round(self.base * 0.21, 2)


class FacturaExentaIncorrecta(Factura):
    @override
    def calcular_iva(self) -> float:
        raise ValueError('Las facturas exentas no tienen IVA')


class FacturaExenta(Factura):
    @override
    def calcular_iva(self) -> float:
        return 0.0


def mostrar_iva(factura: Factura) -> None:
    print('IVA:', factura.calcular_iva())


def main() -> None:
    mostrar_iva(Factura(100.0))
    try:
        mostrar_iva(FacturaExentaIncorrecta(100.0))
    except ValueError as error:
        print('La sustitución rompió el comportamiento esperado:', error)
    mostrar_iva(FacturaExenta(100.0))
    # Un analizador acepta ambas firmas. El contrato de comportamiento requiere pruebas.


if __name__ == '__main__':
    main()
