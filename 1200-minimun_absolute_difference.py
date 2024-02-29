from typing import List


class Solution(object):
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Input: arr = [4,2,1,3]
        Output: [[1,2],[2,3],[3,4]]
        Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
        """
        arr.sort()
        min_diff = float('inf')
        res = []
        for i in range(1, len(arr)):
            min_diff = min(min_diff, abs(arr[i] - arr[i-1]))

        for j in range(1, len(arr)):
            if abs(arr[j] - arr[j-1]) == min_diff:
                res.append([arr[j-1], arr[j]])

        return res



