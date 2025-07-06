from random import random
from entidades.assento import Assento
from entidades.tripulacao import Tripulante
from typing import List

class Voo:
    """
    Representa um voo com destino, assentos e tripulação.
    """

    def __init__(self, id_voo: str, destino: str) -> None:
        self._id_voo: str = id_voo
        self._destino: str = destino
        self._assentos: List[Assento] = [Assento(i + 1) for i in range(250)]
        self._tripulacao: List[Tripulante] = []
        self._preco: float = random.choice([299.90, 399.90, 459.90])

    @property
    def id_voo(self) -> str:
        """Retorna o ID do voo."""
        return self._id_voo

    @property
    def destino(self) -> str:
        """Retorna o destino do voo."""
        return self._destino

    @property
    def assentos(self) -> List[Assento]:
        """Retorna a lista de assentos do voo."""
        return self._assentos

    @property
    def tripulacao(self) -> List[Tripulante]:
        """Retorna a tripulação do voo."""
        return self._tripulacao

    def adicionar_tripulante(self, tripulante: Tripulante) -> None:
        """
        Adiciona um membro à tripulação do voo.
        """
        self._tripulacao.append(tripulante)

    def reservar_assento(self, cliente, numero_assento: str) -> bool:
        """
        Tenta reservar um assento para um cliente.
        :return: True se reservado com sucesso, False caso contrário
        """
        for assento in self._assentos:
            if assento.numero == numero_assento and not assento.ocupado:
                assento.reservar(cliente)
                return True
        return False

    def relatorio_ocupacao(self) -> None:
        """
        Exibe um relatório com o total de assentos ocupados e vagos.
        """
        ocupados: int = sum(1 for a in self._assentos if a.ocupado)
        print(f"Voo {self._id_voo} para {self._destino}:")
        print(f"Assentos ocupados: {ocupados}")
        print(f"Assentos vagos: {250 - ocupados}")
        print(f"Ocupação: {ocupados / 250:.1%}\n")