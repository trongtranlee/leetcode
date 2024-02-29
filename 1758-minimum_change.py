class Solution(object):
    def minOperations(self, s:str)-> int:
        """
        Input: s = "1111"
        Output: 2
        Explanation: You need two operations to reach "0101" or "1010".
        """
        operations = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                operations += 1

        return (operations + 1) // 2

