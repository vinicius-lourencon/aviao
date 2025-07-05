from abc import ABC, abstractmethod

class PessoaBase(ABC):
    """
    Classe base para representar pessoas no sistema.
    """
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str):
        self._nome = nome
        self._cpf = cpf
        self._id = id_
        self._data_nasc = data_nasc

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def id(self) -> str:
        return self._id

    @property
    def data_nasc(self) -> str:
        return self._data_nasc

    @abstractmethod
    def tipo(self) -> str:
        pass