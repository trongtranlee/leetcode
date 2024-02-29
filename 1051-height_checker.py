from typing import List


class Solution(object):
    def heightChecker(self, heights:List[int])-> int:
        """
        Input: heights = [1,1,4,2,1,3]
        Output: 3
        Explanation:
        heights:  [1,1,4,2,1,3]
        expected: [1,1,1,2,3,4]
        Indices 2, 4, and 5 do not match.
        """
        cloneHeight = sorted(heights)
        count = 0
        for key, value in enumerate(heights):
            if heights[key] != cloneHeight[key]:
                count += 1
        return count


