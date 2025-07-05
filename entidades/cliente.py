from entidades.pessoa_base import PessoaBase
from datetime import datetime
from typing import List, Dict

class Cliente(PessoaBase):
    """
    Representa um cliente que pode fazer reservas.
    """

    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str) -> None:
        super().__init__(nome, cpf, id_, data_nasc)
        self._historico_reservas: List[Dict[str, str]] = []

    def tipo(self) -> str:
        """Retorna o tipo da pessoa: Cliente."""
        return "Cliente"

    def adicionar_reserva(self, voo_id: str, destino: str, assento: str) -> None:
        """
        Adiciona uma reserva ao histórico do cliente.

        """
        data: str = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._historico_reservas.append({
            "data": data,
            "voo": voo_id,
            "destino": destino,
            "assento": assento
        })

    def listar_reservas(self) -> None:
        """Exibe todas as reservas feitas pelo cliente."""
        if not self._historico_reservas:
            print("Nenhuma reserva encontrada.")
            return
        for r in self._historico_reservas:
            print(f"Data: {r['data']} | Voo: {r['voo']} | Destino: {r['destino']} | Assento: {r['assento']}")