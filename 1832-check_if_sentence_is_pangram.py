class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in alphabet:
            if char not in sentence:
                return False

        return True