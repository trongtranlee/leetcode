class Solution(object):
    def alternateDigitSum(self, n:int)-> int:
        """
        :type n: int
        :rtype: int
        """
        n_str = str(n)
        total_sum = int(n_str[0])

        for i in range(1, len(n_str)):
            sign = -1 if i % 2 == 1 else 1

            total_sum += sign * int(n_str[i])

        return total_sum
