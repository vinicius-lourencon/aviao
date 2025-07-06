from enum import Enum

class FormaPagamento(Enum):
    CREDITO = "Cartão de Crédito"
    DEBITO = "Cartão de Débito"
    PIX = "PIX"

    def processar(self, valor: float) -> bool:
        """
        Simula o processamento do pagamento. Para fins de teste,
        todo pagamento será aprovado.
        """
        return True
    