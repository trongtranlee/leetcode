from typing import List


class Solution(object):
    def buyChoco(self, prices: List[int], money: int)-> int:
        """
        Input: prices = [1,2,2], money = 3
        Output: 0
        Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.
        """
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        return money
