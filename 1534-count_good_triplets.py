from typing import List


class Solution(object):
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
        Output: 4
        Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
        """
        count = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
