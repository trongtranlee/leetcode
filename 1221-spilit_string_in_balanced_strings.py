from collections import Counter


class Solution(object):
    def balancedStringSplit(self, s:str)-> int:
        """
        Input: s = "RLRRLLRLRL"
        Output: 4
        Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
        """
        balance = 0
        count = 0

        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count


