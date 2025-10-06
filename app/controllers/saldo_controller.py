from decimal import Decimal

from app.schemas.saldo import SaldoResponse


class SaldoController:
    """Controller for balance operations"""

    @staticmethod
    def consultar_saldo(usuario_id: int) -> SaldoResponse:
        """
        Get user balance

        Args:
            usuario_id: User ID

        Returns:
            SaldoResponse: User balance information
        """
        # TODO: Implement database query for balance
        saldo_disponivel = Decimal("1000.00")
        saldo_bloqueado = Decimal("50.00")

        return SaldoResponse(
            usuario_id=usuario_id,
            saldo_disponivel=saldo_disponivel,
            saldo_bloqueado=saldo_bloqueado,
            saldo_total=saldo_disponivel + saldo_bloqueado,
        )
