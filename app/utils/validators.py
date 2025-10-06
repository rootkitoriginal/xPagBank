"""
Validators utility module

Funções de validação reutilizáveis para CPF, CNPJ, Email e Username.
Compartilhado entre controllers V1 e V2.
"""
import re


class Validators:
    """Classe com métodos estáticos para validação de documentos e email"""

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Valida um CPF brasileiro

        Args:
            cpf: CPF com ou sem formatação

        Returns:
            True se válido, False caso contrário

        Examples:
            >>> Validators.validar_cpf("123.456.789-09")
            False
            >>> Validators.validar_cpf("12345678909")
            False
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r"\D", "", cpf)

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Valida primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        if int(cpf[9]) != digito1:
            return False

        # Valida segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return int(cpf[10]) == digito2

    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        """
        Valida um CNPJ brasileiro

        Args:
            cnpj: CNPJ com ou sem formatação

        Returns:
            True se válido, False caso contrário

        Examples:
            >>> Validators.validar_cnpj("12.345.678/0001-90")
            False
            >>> Validators.validar_cnpj("12345678000190")
            False
        """
        # Remove caracteres não numéricos
        cnpj = re.sub(r"\D", "", cnpj)

        # Verifica se tem 14 dígitos
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais
        if cnpj == cnpj[0] * 14:
            return False

        # Valida primeiro dígito verificador
        multiplicadores1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores1[i] for i in range(12))
        digito1 = 11 - (soma % 11)
        digito1 = 0 if digito1 > 9 else digito1

        if int(cnpj[12]) != digito1:
            return False

        # Valida segundo dígito verificador
        multiplicadores2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * multiplicadores2[i] for i in range(13))
        digito2 = 11 - (soma % 11)
        digito2 = 0 if digito2 > 9 else digito2

        return int(cnpj[13]) == digito2

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Valida um endereço de email

        Args:
            email: Email a ser validado

        Returns:
            True se válido, False caso contrário

        Examples:
            >>> Validators.validar_email("usuario@example.com")
            True
            >>> Validators.validar_email("email_invalido")
            False
        """
        padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(padrao, email))

    @staticmethod
    def validar_username(username: str) -> bool:
        """
        Valida se o username é CPF, CNPJ ou Email válido

        Args:
            username: CPF, CNPJ ou Email

        Returns:
            True se válido, False caso contrário

        Examples:
            >>> Validators.validar_username("usuario@example.com")
            True
            >>> Validators.validar_username("123.456.789-09")
            # Depende se é CPF válido
        """
        # Remove espaços em branco
        username = username.strip()

        # Verifica se é email
        if "@" in username:
            return Validators.validar_email(username)

        # Remove caracteres não numéricos para testar CPF/CNPJ
        apenas_numeros = re.sub(r"\D", "", username)

        # Verifica se é CPF (11 dígitos)
        if len(apenas_numeros) == 11:
            return Validators.validar_cpf(username)

        # Verifica se é CNPJ (14 dígitos)
        if len(apenas_numeros) == 14:
            return Validators.validar_cnpj(username)

        return False

    @staticmethod
    def identificar_tipo(username: str) -> str:
        """
        Identifica o tipo de username (CPF, CNPJ ou Email)

        Args:
            username: CPF, CNPJ ou Email

        Returns:
            'cpf', 'cnpj', 'email' ou 'unknown'

        Examples:
            >>> Validators.identificar_tipo("usuario@example.com")
            'email'
            >>> Validators.identificar_tipo("12345678909")
            'cpf'
        """
        username = username.strip()

        # Verifica se é email
        if "@" in username and Validators.validar_email(username):
            return "email"

        # Remove caracteres não numéricos
        apenas_numeros = re.sub(r"\D", "", username)

        # Verifica se é CPF (11 dígitos)
        if len(apenas_numeros) == 11 and Validators.validar_cpf(username):
            return "cpf"

        # Verifica se é CNPJ (14 dígitos)
        if len(apenas_numeros) == 14 and Validators.validar_cnpj(username):
            return "cnpj"

        return "unknown"
