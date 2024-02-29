from collections import Counter


class Solution(object):
    def numJewelsInStones(self, jewels:str, stones:str)-> int:
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count_stone = Counter(stones)
        count = 0
        for key, value in count_stone.items():
            if key in jewels:
                count += value
        return count

