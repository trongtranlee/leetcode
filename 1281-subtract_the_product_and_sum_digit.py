class Solution(object):
    def subtractProductAndSum(self, n:int)-> int:
        """
        Input: n = 234
        Output: 15
        Explanation:
        Product of digits = 2 * 3 * 4 = 24
        Sum of digits = 2 + 3 + 4 = 9
        Result = 24 - 9 = 15
        """
        product = 1
        total = 0
        for digit in str(n):
            product *= int(digit)
            total += int(digit)
        return product - total

