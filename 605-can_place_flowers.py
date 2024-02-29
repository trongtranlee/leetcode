from astroid import List


class Solution(object):
    def canPlaceFlowers(self, flowerbed:List[int], n:int)-> bool:
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n

