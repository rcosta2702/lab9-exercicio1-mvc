from decimal import Decimal

from models.banco_dados import BancoDados
from models.cliente import Cliente
from models.conta import Conta
from views.conta_view import ContaView


class ContaController:
    def __init__(self, banco: BancoDados, view: ContaView) -> None:
        self.banco = banco
        self.view = view
        self.view.ao_criar(self._criar_pela_view)
        self.view.ao_consultar(self._consultar_pela_view)

    def criar_conta(self, nome: str, cpf: str, saldo_inicial: Decimal) -> Conta:
        cliente = Cliente(nome=nome, cpf=cpf)
        conta = Conta(
            numero=len(self.banco.listar()) + 1,
            cliente=cliente,
            saldo=saldo_inicial,
        )
        self.banco.salvar(conta)
        return conta

    def consultar_conta(self, numero: int) -> Conta:
        conta = self.banco.buscar(numero)
        if conta is None:
            raise ValueError("Conta nao encontrada.")
        return conta

    def executar(self) -> None:
        self.view.iniciar()

    def _criar_pela_view(self) -> None:
        try:
            nome, cpf, saldo = self.view.ler_dados_conta()
            conta = self.criar_conta(nome, cpf, saldo)
            self.view.selecionar_conta(conta.numero)
            self.view.exibir_conta(conta, "Conta criada com sucesso!")
        except ValueError as exc:
            self.view.exibir_erro(str(exc))

    def _consultar_pela_view(self) -> None:
        try:
            conta = self.consultar_conta(self.view.ler_numero_conta())
            self.view.exibir_conta(conta, "Dados da conta")
        except ValueError as exc:
            self.view.exibir_erro(str(exc))
