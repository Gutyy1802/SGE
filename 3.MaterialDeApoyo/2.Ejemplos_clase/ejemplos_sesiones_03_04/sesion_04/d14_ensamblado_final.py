"""Guion S4, diapositiva 14: componer repositorio en memoria y aplicación."""
from d11_inversion_dependencias import RepositorioEnMemoria
from d12_inyeccion_constructor import ServicioProcesamientoFactura


def main() -> None:
    # 1. Crear la implementación concreta del almacenamiento simulado.
    repo: RepositorioEnMemoria = RepositorioEnMemoria()
    # 2. Inyectarla en el servicio, que depende del contrato abstracto.
    servicio: ServicioProcesamientoFactura = ServicioProcesamientoFactura(repo)
    # 3. Ejecutar la operación de negocio.
    print('Guardado:', servicio.procesar('FAC-2026-001', {'total': 1500.0}))
    print('Lectura del almacenamiento simulado:', repo.facturas)
    # Los datos solo existen durante esta ejecución, no se escribe ningún archivo.


if __name__ == '__main__':
    main()
