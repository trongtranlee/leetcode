from typing import List


class Solution(object):
    def minSubsequence(self, nums:List[int])-> List[int]:
        """
        Input: nums = [4,3,10,9,8]
        Output: [10,9]
        Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than
        the sum of elements not included. However, the subsequence [10,9] has the maximum total sum of its elements.
        """
        res = []
        if not nums:
            return res
        elif len(nums) < 3 and len(set(nums)) != 1:
            res.append(max(nums))
            return res
        elif len(set(nums)) == 1:
            return nums

        nums.sort(reverse=True)
        total_sum = sum(nums)
        subsequence_sum = 0
        remaining_sum = total_sum
        for num in nums:
            subsequence_sum += num
            remaining_sum -= num
            res.append(num)
            if subsequence_sum > remaining_sum:
                return res
        return res

