"""Guion S4, diapositiva 12: inyección por constructor y rechazo de guardado."""
from typing import override
from d11_inversion_dependencias import DatosFactura, RepositorioEnMemoria, RepositorioFacturas


class ServicioProcesamientoFactura:
    def __init__(self, repositorio: RepositorioFacturas) -> None:
        self.repositorio: RepositorioFacturas = repositorio

    def procesar(self, factura_id: str, datos: DatosFactura) -> bool:
        return self.repositorio.guardar(factura_id, datos)


class RepositorioQueRechaza(RepositorioFacturas):
    @override
    def guardar(self, factura_id: str, datos: DatosFactura) -> bool:
        return False  # Otro comportamiento contemplado por el contrato bool.


def main() -> None:
    repo: RepositorioEnMemoria = RepositorioEnMemoria()
    servicio: ServicioProcesamientoFactura = ServicioProcesamientoFactura(repo)
    print('Guardado:', servicio.procesar('FAC-001', {'total': 1500.0}))
    print('Memoria:', repo.facturas)
    otro_servicio: ServicioProcesamientoFactura = ServicioProcesamientoFactura(RepositorioQueRechaza())
    print('Rechazado:', otro_servicio.procesar('FAC-002', {'total': 50.0}))


if __name__ == '__main__':
    main()
