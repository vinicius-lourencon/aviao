from abc import ABC, abstractmethod

class PessoaBase(ABC):
    """
    Classe base abstrata para representar uma pessoa no sistema.
    """
    def __init__(self, nome: str):
        self._nome: str = nome

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @abstractmethod
    def tipo(self) -> str:
        """
        Retorna o tipo da pessoa (ex: Cliente, Tripulante).
        """
        pass
