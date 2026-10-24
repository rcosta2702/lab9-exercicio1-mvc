import tkinter as tk
from decimal import Decimal, InvalidOperation
from tkinter import messagebox, ttk
from typing import Callable

from models.conta import Conta


class ContaView:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Exercicio 1 - MVC Bancario")
        self.root.geometry("520x540")
        self.root.resizable(False, False)

        quadro = ttk.Frame(self.root, padding=24)
        quadro.pack(fill="both", expand=True)
        ttk.Label(quadro, text="Cadastro de conta", font=("Segoe UI", 18, "bold")).pack(pady=(0, 18))

        self.nome = self._campo(quadro, "Nome")
        self.cpf = self._campo(quadro, "CPF")
        self.saldo = self._campo(quadro, "Saldo inicial (R$)")
        self.botao_criar = ttk.Button(quadro, text="Criar conta")
        self.botao_criar.pack(fill="x", pady=(8, 16))

        consulta = ttk.LabelFrame(quadro, text="Exibir dados da conta", padding=12)
        consulta.pack(fill="x", pady=(0, 14))
        ttk.Label(consulta, text="Numero da conta").pack(anchor="w")
        self.numero_consulta = ttk.Entry(consulta)
        self.numero_consulta.pack(fill="x", pady=(2, 8))
        self.botao_consultar = ttk.Button(consulta, text="Exibir dados")
        self.botao_consultar.pack(fill="x")

        self.resultado = tk.Text(quadro, height=8, state="disabled", font=("Consolas", 10))
        self.resultado.pack(fill="both", expand=True)

    @staticmethod
    def _campo(pai: ttk.Frame, rotulo: str) -> ttk.Entry:
        ttk.Label(pai, text=rotulo).pack(anchor="w")
        entrada = ttk.Entry(pai)
        entrada.pack(fill="x", pady=(2, 10))
        return entrada

    def ao_criar(self, callback: Callable[[], None]) -> None:
        self.botao_criar.configure(command=callback)

    def ao_consultar(self, callback: Callable[[], None]) -> None:
        self.botao_consultar.configure(command=callback)

    def ler_dados_conta(self) -> tuple[str, str, Decimal]:
        try:
            saldo = Decimal(self.saldo.get().replace(",", "."))
        except InvalidOperation as exc:
            raise ValueError("Saldo inicial invalido.") from exc
        return self.nome.get().strip(), self.cpf.get().strip(), saldo

    def ler_numero_conta(self) -> int:
        try:
            return int(self.numero_consulta.get())
        except ValueError as exc:
            raise ValueError("Numero da conta invalido.") from exc

    def selecionar_conta(self, numero: int) -> None:
        self.numero_consulta.delete(0, "end")
        self.numero_consulta.insert(0, str(numero))

    def exibir_conta(self, conta: Conta, titulo: str = "Dados da conta") -> None:
        texto = (
            f"{titulo}\n\n"
            f"Numero: {conta.numero}\n"
            f"Cliente: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Saldo: R$ {conta.saldo:.2f}"
        )
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)
        self.resultado.configure(state="disabled")

    def exibir_erro(self, mensagem: str) -> None:
        messagebox.showerror("Erro", mensagem, parent=self.root)

    def iniciar(self) -> None:
        self.nome.focus_set()
        self.root.mainloop()
