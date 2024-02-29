from typing import List


class Solution(object):
    def numIdenticalPairs(self, nums:List[int])-> int:
        """
        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
        """
        count = 0
        occurrences = {}

        for num in nums:
            if num in occurrences:
                count += occurrences[num]
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        return count
