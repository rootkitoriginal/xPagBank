from datetime import datetime

from app.schemas.usuario import UsuarioCreate, UsuarioResponse


class UsuarioController:
    """Controller for user operations"""

    @staticmethod
    def criar_usuario(usuario_data: UsuarioCreate) -> UsuarioResponse:
        """
        Create a new user

        Args:
            usuario_data: User creation data

        Returns:
            UsuarioResponse: Created user data
        """
        # TODO: Implement database logic
        # Mock response for now
        return UsuarioResponse(
            id=1,
            nome=usuario_data.nome,
            email=usuario_data.email,
            cpf=usuario_data.cpf,
            telefone=usuario_data.telefone,
            ativo=True,
            data_criacao=datetime.now(),
        )
