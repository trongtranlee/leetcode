from astroid import List


class Solution(object):
    def search(self, nums:List[int], target:int)-> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hashMap = {}
        for key, value in enumerate(nums):
            hashMap[value] = key  # Chuyển đổi từ key-value sang value-key

        if target in hashMap: 
            return hashMap[target]  # Trả về index của target
        return -1

