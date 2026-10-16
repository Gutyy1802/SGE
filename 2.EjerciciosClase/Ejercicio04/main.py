from dominio import Factura, LineaFactura
from impuestos import ImpuestoGeneral, ImpuestoReducido, ImpuestoRecargo
 
def main() -> None:
    factura = Factura(
        "F-001",
        "Comercial Aula SL",
        "B12345678",
        (LineaFactura("Licencia ERP", 1, 1500.0), LineaFactura("Soporte", 2, 250.0)),
    )

    for calculador, esperando in ((ImpuestoGeneral(), 2420.0),
                                (ImpuestoReducido(), 2420.0), 
                                (ImpuestoRecargo(), 2420.0)):
        total = factura.base_imponible + calculador.calcular_impuesto(factura.base_imponible)
 
    assert factura.base_imponible == 2000.0
    try:
        Factura("F-002", "Comercial Aula SL", "B12345678", ())
    except ValueError:
        print("Factura vacía rechazada")
    else:
        raise AssertionError("No se rechazó la factura vacía")
    print(f"Base: {factura.base_imponible:.2f}")