from typing import List


class Solution(object):
    def intersection(self, nums:List[List[int]])->List[int]:
        """
        Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
        Output: [3,4]
        Explanation:
        The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4,
        so we return [3,4].
        """
        common_set = set(nums[0])

        for arr in nums[1:]:
            common_set.intersection_update(set(arr))

        common_list = sorted(common_set)

        return common_list

