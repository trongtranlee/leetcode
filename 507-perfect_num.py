from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num:int)-> bool:
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        divisor_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:  # Kiểm tra nếu i không phải là căn bậc hai của num
                    divisor_sum += num // i

        return divisor_sum == num


