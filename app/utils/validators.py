"""
Validators for user inputs
"""
import re


class Validators:
    """Validation utilities"""

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Validate CPF format
        
        Args:
            cpf: CPF string (can contain dots and dashes)
            
        Returns:
            True if valid, False otherwise
        """
        # Remove non-numeric characters
        cpf = re.sub(r'\D', '', cpf)
        
        # Check if it has 11 digits
        if len(cpf) != 11:
            return False
            
        # Check if all digits are the same
        if cpf == cpf[0] * 11:
            return False
            
        # Validate first check digit
        sum_value = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit1 = (sum_value * 10 % 11) % 10
        
        if int(cpf[9]) != digit1:
            return False
            
        # Validate second check digit
        sum_value = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digit2 = (sum_value * 10 % 11) % 10
        
        if int(cpf[10]) != digit2:
            return False
            
        return True

    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        """
        Validate CNPJ format
        
        Args:
            cnpj: CNPJ string (can contain dots, dashes and slashes)
            
        Returns:
            True if valid, False otherwise
        """
        # Remove non-numeric characters
        cnpj = re.sub(r'\D', '', cnpj)
        
        # Check if it has 14 digits
        if len(cnpj) != 14:
            return False
            
        # Check if all digits are the same
        if cnpj == cnpj[0] * 14:
            return False
            
        # Validate first check digit
        weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_value = sum(int(cnpj[i]) * weights1[i] for i in range(12))
        digit1 = (sum_value % 11)
        digit1 = 0 if digit1 < 2 else 11 - digit1
        
        if int(cnpj[12]) != digit1:
            return False
            
        # Validate second check digit
        weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_value = sum(int(cnpj[i]) * weights2[i] for i in range(13))
        digit2 = (sum_value % 11)
        digit2 = 0 if digit2 < 2 else 11 - digit2
        
        if int(cnpj[13]) != digit2:
            return False
            
        return True

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Validate email format
        
        Args:
            email: Email string
            
        Returns:
            True if valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validar_username(username: str) -> bool:
        """
        Validate username (can be CPF, CNPJ or Email)
        
        Args:
            username: Username string
            
        Returns:
            True if valid, False otherwise
        """
        if not username:
            return False
            
        # Try CPF
        if Validators.validar_cpf(username):
            return True
            
        # Try CNPJ
        if Validators.validar_cnpj(username):
            return True
            
        # Try Email
        if Validators.validar_email(username):
            return True
            
        return False
