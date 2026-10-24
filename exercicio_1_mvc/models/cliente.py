from dataclasses import dataclass


@dataclass(frozen=True)
class Cliente:
    nome: str
    cpf: str

    def __post_init__(self) -> None:
        if not self.nome.strip():
            raise ValueError("O nome e obrigatorio.")
        if not self.cpf.strip():
            raise ValueError("O CPF e obrigatorio.")
