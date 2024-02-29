class Solution(object):
    def areOccurrencesEqual(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        Input: s = "abacbc"
        Output: true
        Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
        """
        hashtable = {}
        for char in s:
            hashtable[char] = s.count(char)
        freg = hashtable.values()
        first_value = freg[0]
        for value in freg[1:]:
            if value != first_value:
                return False
        return True
