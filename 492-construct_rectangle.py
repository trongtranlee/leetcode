from typing import List


class Solution(object):
    def constructRectangle(self, area: int) -> List[int]:
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt_area = int(area ** 0.5)
        for width in range(sqrt_area, 0, -1):
            if area % width == 0:
                length = area // width
                return [length, width]
