class Solution(object):
    def findTheLongestBalancedSubstring(self, s:str)-> int:
        """
        Input: s = "01000111"
        Output: 6
        Explanation: The longest balanced substring is "000111", which has length 6.
        """
        temp = '01'
        while temp in s:
            temp = '0' + temp + '1'
        return len(temp) - 2
