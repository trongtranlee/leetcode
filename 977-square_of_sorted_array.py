from astroid import List


class Solution(object):
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].
        """
        squared_nums = []
        for num in nums:
            squared_nums.append(num ** 2)
        squared_nums.sort()
        return squared_nums
