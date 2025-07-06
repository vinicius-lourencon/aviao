import uuid
from datetime import datetime
from pagamento.forma_pagamento import FormaPagamento
from pagamento.status_pagamento import StatusPagamento

class Pagamento:
    """
    Representa uma transação de pagamento.
    """

    def __init__(self, forma: FormaPagamento) -> None:
        self.id_pagamento = uuid.uuid4()
        self.forma = forma
        self.status = StatusPagamento.PENDENTE
        self.data_transacao = None

    def realizar_pagamento(self, valor: float) -> bool:
        """
        Processa o pagamento com base na forma escolhida.
        """
        aprovado = self.forma.processar(valor)
        self.data_transacao = datetime.now()
        self.status = StatusPagamento.APROVADO if aprovado else StatusPagamento.RECUSADO
        return aprovado

    def __str__(self) -> str:
        return (f"Pagamento via {self.forma.value} | "
                f"Status: {self.status.value} | "
                f"Data: {self.data_transacao.strftime('%d/%m/%Y %H:%M:%S') if self.data_transacao else 'N/A'}")