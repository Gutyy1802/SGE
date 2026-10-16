"""Guion S4, diapositiva 10: consumidores que dependen de protocolos pequeños."""
from typing import Protocol, TypedDict


class Datos(TypedDict):
    cliente: str
    total: float


class CargadorDatos(Protocol):
    def cargar(self) -> Datos: ...


class GuardadorDatos(Protocol):
    def guardar(self, datos: Datos) -> bool: ...


class FuenteSoloLectura:
    def cargar(self) -> Datos:
        return {'cliente': 'CLI-001', 'total': 121.0}


class DestinoSoloEscritura:
    def guardar(self, datos: Datos) -> bool:
        print('Guardado simulado:', datos)
        return True


def mostrar_resumen(fuente: CargadorDatos) -> None:
    datos: Datos = fuente.cargar()
    print(f"Cliente {datos['cliente']}, total {datos['total']:.2f}")


def copiar(fuente: CargadorDatos, destino: GuardadorDatos) -> bool:
    return destino.guardar(fuente.cargar())


def main() -> None:
    fuente: FuenteSoloLectura = FuenteSoloLectura()
    mostrar_resumen(fuente)
    print(copiar(fuente, DestinoSoloEscritura()))
    # FuenteSoloLectura no tiene que implementar guardar ni un método vacío.


if __name__ == '__main__':
    main()
