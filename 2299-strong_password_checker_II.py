class Solution(object):
    def strongPasswordCheckerII(self, password:str)-> bool:
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        special_characters = "!@#$%^&*()-+"
        if not any(char in special_characters for char in password):
            return False
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        return True
