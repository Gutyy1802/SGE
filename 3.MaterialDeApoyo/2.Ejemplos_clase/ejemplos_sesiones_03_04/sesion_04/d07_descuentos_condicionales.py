"""Guion S4, diapositiva 7: nuevos descuentos obligan a editar la función."""


def aplicar_descuento(cliente_tipo: str, total: float) -> float:
    if cliente_tipo == 'VIP':
        return total * 0.80
    if cliente_tipo == 'EMPLEADO':
        return total * 0.70
    if cliente_tipo == 'AGENCIA':
        return total * 0.85
    return total


def main() -> None:
    tipos: tuple[str, ...] = ('VIP', 'EMPLEADO', 'AGENCIA', 'GENERAL')
    for tipo in tipos:
        print(f'{tipo}: {aplicar_descuento(tipo, 100.0):.2f}')
    print('Para añadir MAYORISTA tendríamos que modificar aplicar_descuento.')


if __name__ == '__main__':
    main()
