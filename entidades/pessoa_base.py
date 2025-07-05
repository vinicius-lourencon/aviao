from abc import ABC, abstractmethod

class PessoaBase(ABC):
    """
    Classe base para representar pessoas no sistema.
    """

    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str) -> None:
        self._nome: str = nome
        self._cpf: str = cpf
        self._id: str = id_
        self._data_nasc: str = data_nasc

    @property
    def nome(self) -> str:
        """Retorna o nome da pessoa."""
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        """Altera o nome da pessoa."""
        self._nome = novo_nome

    @property
    def cpf(self) -> str:
        """Retorna o CPF da pessoa."""
        return self._cpf

    @property
    def id(self) -> str:
        """Retorna o ID da pessoa."""
        return self._id

    @property
    def data_nasc(self) -> str:
        """Retorna a data de nascimento."""
        return self._data_nasc

    @abstractmethod
    def tipo(self) -> str:
        """Define o tipo da pessoa (cliente ou tripulante)."""
        pass