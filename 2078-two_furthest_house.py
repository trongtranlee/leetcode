from typing import List


class Solution(object):
    def maxDistance(self, colors: List[int]) -> int:
        """
        Input: colors = [1,8,3,8,3]
        Output: 4
        Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
        The furthest two houses with different colors are house 0 and house 4.
        House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
        """
        max_lockside = 0
        max_counter_lockside = 0
        left1 = 0
        right1 = len(colors) - 1
        while left1 < right1:
            if colors[left1] != colors[right1]:
                max_lockside = max(max_lockside, right1 - left1)
            right1 -= 1

        left2 = 0
        right2 = len(colors) - 1
        while left2 < right2:
            if colors[left2] != colors[right2]:
                max_counter_lockside = max(max_counter_lockside, right2 - left2)
            left2 += 1

        return max(max_lockside, max_counter_lockside)
