from astroid import List


class Solution(object):
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def shoelace_formula(p1, p2, p3):
            return 0.5 * abs(
                p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1])

        max_area = 0
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    area = shoelace_formula(points[i], points[j], points[k])
                    max_area = max(max_area, area)
        return max_area
