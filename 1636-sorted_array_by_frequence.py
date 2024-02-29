from typing import List


class Solution(object):
    def frequencySort(self, nums:List[int])-> List[int]:
        """
        Input: nums = [1,1,2,2,2,3]
        Output: [3,1,1,2,2,2]
        freg = [3:1, 1:2, 2:3]
        Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
        """
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_nums = sorted(nums, key=lambda x: (freq_map[x], -x))

        return sorted_nums
