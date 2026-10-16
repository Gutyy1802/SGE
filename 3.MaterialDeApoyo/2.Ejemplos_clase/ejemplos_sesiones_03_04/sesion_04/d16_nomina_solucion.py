"""Solución S4, diapositivas 15-16: cálculo puro, contrato y servicio.

La retención fija es una regla didáctica del guion, no un cálculo fiscal real.
"""
from abc import ABC, abstractmethod
from typing import override


class RepositorioNomina(ABC):
    @abstractmethod
    def guardar(self, empleado: str, neto: float) -> bool:
        raise NotImplementedError


class CalculadorNomina:
    @staticmethod
    def calcular_neto(base: float, irpf: float = 19.0) -> float:
        return round(base * (1 - irpf / 100), 2)


class ServicioNomina:
    def __init__(self, repo: RepositorioNomina) -> None:
        self.repo: RepositorioNomina = repo

    def procesar(self, empleado: str, base: float) -> bool:
        neto: float = CalculadorNomina.calcular_neto(base)
        return self.repo.guardar(empleado, neto)


class RepositorioNominaEnMemoria(RepositorioNomina):
    def __init__(self) -> None:
        self.nominas: dict[str, float] = {}

    @override
    def guardar(self, empleado: str, neto: float) -> bool:
        self.nominas[empleado] = neto
        return True


class RepositorioNominaConsola(RepositorioNomina):
    @override
    def guardar(self, empleado: str, neto: float) -> bool:
        print(f'Guardado simulado: {empleado}, neto {neto:.2f}')
        return True


def main() -> None:
    repo: RepositorioNominaEnMemoria = RepositorioNominaEnMemoria()
    servicio: ServicioNomina = ServicioNomina(repo)
    print('Guardado:', servicio.procesar('Ana', 2000.0))
    print('Nóminas:', repo.nominas)
    print('Otra tasa didáctica:', CalculadorNomina.calcular_neto(2000.0, irpf=10.0))
    # El servicio permanece igual al sustituir la infraestructura.
    otro_servicio: ServicioNomina = ServicioNomina(RepositorioNominaConsola())
    print('Otro repositorio:', otro_servicio.procesar('Luis', 1500.0))


if __name__ == '__main__':
    main()
