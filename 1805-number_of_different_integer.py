class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        clean_word = ''.join(c if c.isdigit() else ' ' for c in word)
        integers = clean_word.split()
        integers = [int(integer) for integer in integers]
        unique_integers = set(integers)
        return len(unique_integers)