"""Mini-reto S4, diapositiva 15: refactorizar mediante SRP y DIP.

1. Crear el método abstracto guardar(empleado: str, neto: float) -> bool.
2. Completar calcular_neto: retención del 19 %, redondeo a 2 decimales.
3. ServicioNomina recibe un repositorio por constructor, calcula y delega.
4. Crear RepositorioNominaEnMemoria que herede del contrato.
5. Procesar Ana, base 2000.0: resultado True y neto guardado 1620.0.

No importar la solución. Los TODO lanzan NotImplementedError hasta completarse.
"""
from abc import ABC


class CalculadorNominaMonolitico:
    def procesar_nomina(self, empleado: str, salario_base: float) -> None:
        neto: float = salario_base * 0.81
        # SQL únicamente mostrado, nunca ejecutado.
        print(f"Simulación: INSERT INTO nominas VALUES ('{empleado}', {neto})")


class RepositorioNomina(ABC):
    # TODO: declarar guardar como abstractmethod, con parámetros y retorno tipados.
    pass


class CalculadorNomina:
    @staticmethod
    def calcular_neto(base: float, irpf: float = 19.0) -> float:
        # TODO: calcular el neto y redondearlo a 2 decimales.
        raise NotImplementedError('Completa calcular_neto')


class ServicioNomina:
    def __init__(self, repo: RepositorioNomina) -> None:
        # TODO: guardar la dependencia con anotación de tipo.
        raise NotImplementedError('Completa __init__')

    def procesar(self, empleado: str, base: float) -> bool:
        # TODO: calcular el neto y devolver el resultado del repositorio.
        raise NotImplementedError('Completa procesar')


def main() -> None:
    print('Código original a refactorizar:')
    CalculadorNominaMonolitico().procesar_nomina('Ana', 2000.0)
    print('Completa los TODO y sustituye esta demostración por el flujo refactorizado.')
    # TODO: instanciar tu repositorio concreto, inyectarlo y mostrar el neto guardado.


if __name__ == '__main__':
    main()
