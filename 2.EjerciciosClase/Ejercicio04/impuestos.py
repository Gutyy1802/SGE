from abc import ABC, abstractmethod


class CalculadorImpuesto(ABC):
    @abstractmethod
    def calcular_impuesto(self, base: float) -> float:
        ...

class Impuestogeneral(CalculadorImpuesto):
    def calcular_impuesto(self, base):
        return round(base * 0.21, 2)

class ImpuestoReducido(CalculadorImpuesto):
    def calcular_impuesto(self, base):
        return round(base * 0.10, 2)

class ImpuestoRecargo(CalculadorImpuesto):
    def calcular_impuesto(self, base):
        return round(base * 0.262, 2)