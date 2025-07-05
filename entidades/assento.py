class Assento:
    """
    Representa um assento do voo.
    """

    def __init__(self, numero: str) -> None:
        self._numero: str = numero
        self._ocupado: bool = False
        self._cliente = None

    def reservar(self, cliente) -> None:
        """
        Reserva o assento para um cliente.

        """
        self._ocupado = True
        self._cliente = cliente

    @property
    def numero(self) -> str:
        """Retorna o número do assento."""
        return self._numero

    @property
    def ocupado(self) -> bool:
        """Indica se o assento está ocupado."""
        return self._ocupado

    @property
    def cliente(self):
        """Retorna o cliente associado ao assento (se houver)."""
        return self._cliente