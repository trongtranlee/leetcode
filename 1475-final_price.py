from typing import List


class Solution(object):
    def finalPrices(self, prices:List[int])->List[int]:
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prev_index = stack.pop()
                prices[prev_index] -= price

            result.append(prices[i])
            stack.append(i)

        return result
