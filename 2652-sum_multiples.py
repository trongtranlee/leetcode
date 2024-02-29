class Solution(object):
    def sumOfMultiples(self, n:int)-> int:
        """
        Input: n = 7
        Output: 21
        Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
        """
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total = total + i
        return total
