class Solution(object):
    def detectCapitalUse(self, word:str)-> bool:
        """
        :type word: str
        :rtype: bool
        """
        # Check if all letters in the word are capitals
        if word.isupper():
            return True
        # Check if all letters in the word are lowercase
        elif word.islower():
            return True
        # Check if only the first letter in the word is capital
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
