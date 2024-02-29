class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        current_day = 1
        amount = 1

        for i in range(n):
            total += amount
            current_day += 1
            if current_day == 8:
                amount += 1
                current_day = 1

        return total
