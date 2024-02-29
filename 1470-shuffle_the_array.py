from typing import List


class Solution(object):
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Input: nums = [2,5,1,3,4,7], n = 3
        Output: [2,3,5,4,1,7]
        Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
        """
        n = len(nums) // 2
        result = []

        even_elements = nums[:n]
        odd_elements = nums[n:]

        for i in range(n):
            result.append(even_elements[i])
            result.append(odd_elements[i])

        return result

