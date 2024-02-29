from astroid import List


class Solution(object):
    def distributeCandies(self, candyType:List[int])-> int:
        """
        :type candyType: List[int]
        :rtype: int
        """
        max_types = len(set(candyType))
        return min(max_types, len(candyType) // 2)
