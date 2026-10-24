from dataclasses import dataclass
from decimal import Decimal

from models.cliente import Cliente


@dataclass
class Conta:
    numero: int
    cliente: Cliente
    saldo: Decimal

    def __post_init__(self) -> None:
        self.saldo = Decimal(str(self.saldo))
        if self.saldo < 0:
            raise ValueError("O saldo inicial nao pode ser negativo.")
