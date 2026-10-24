from models.conta import Conta


class BancoDados:
    """Banco de dados simulado por uma lista em memoria."""

    def __init__(self) -> None:
        self._contas: list[Conta] = []

    def salvar(self, conta: Conta) -> None:
        self._contas.append(conta)

    def buscar(self, numero: int) -> Conta | None:
        return next((conta for conta in self._contas if conta.numero == numero), None)

    def listar(self) -> list[Conta]:
        return list(self._contas)
