from entidades.pessoa_base import PessoaBase

class Tripulante(PessoaBase):
    """
    Representa um membro da tripulação de voo.
    """

    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str, funcao: str) -> None:
        super().__init__(nome, cpf, id_, data_nasc)
        self._funcao: str = funcao

    def tipo(self) -> str:
        """Retorna o tipo da pessoa: Tripulante."""
        return "Tripulante"

    @property
    def funcao(self) -> str:
        """Retorna a função do tripulante (piloto, comissário, etc.)."""
        return self._funcao


class Piloto(Tripulante):
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str) -> None:
        """Cria um Piloto."""
        super().__init__(nome, cpf, id_, data_nasc, "Piloto")


class Copiloto(Tripulante):
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str) -> None:
        """Cria um Copiloto."""
        super().__init__(nome, cpf, id_, data_nasc, "Copiloto")


class Comissario(Tripulante):
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str) -> None:
        """Cria um Comissário de bordo."""
        super().__init__(nome, cpf, id_, data_nasc, "Comissário")