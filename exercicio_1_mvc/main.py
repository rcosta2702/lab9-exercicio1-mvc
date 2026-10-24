from controllers.conta_controller import ContaController
from models.banco_dados import BancoDados
from views.conta_view import ContaView


def main() -> None:
    ContaController(BancoDados(), ContaView()).executar()


if __name__ == "__main__":
    main()
