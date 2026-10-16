"""Guion S4, diapositiva 11: dominio y almacenamiento dependen del contrato."""
from abc import ABC, abstractmethod
from typing import TypedDict, override


class DatosFactura(TypedDict):
    total: float


class RepositorioFacturas(ABC):
    @abstractmethod
    def guardar(self, factura_id: str, datos: DatosFactura) -> bool:
        raise NotImplementedError


class RepositorioEnMemoria(RepositorioFacturas):
    def __init__(self) -> None:
        self.facturas: dict[str, DatosFactura] = {}

    @override
    def guardar(self, factura_id: str, datos: DatosFactura) -> bool:
        self.facturas[factura_id] = datos.copy()
        return True


def registrar(repo: RepositorioFacturas, factura_id: str, total: float) -> bool:
    # La función no crea ni importa una conexión SQL.
    return repo.guardar(factura_id, {'total': total})


def main() -> None:
    repo: RepositorioEnMemoria = RepositorioEnMemoria()
    print(registrar(repo, 'FAC-001', 121.0))
    print(repo.facturas)


if __name__ == '__main__':
    main()
