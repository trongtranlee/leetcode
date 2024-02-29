class Solution(object):
    def removePalindromeSub(self, s:str)-> int:
        """
        Input: s = "baabb"
        Output: 2
        Explanation: "baabb" -> "b" -> "".
        Remove palindromic subsequence "baab" then "b".
        """
        if not s:
            return 0

        if s == s[::-1]:
            return 1

        return 2

