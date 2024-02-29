from typing import List


class Solution(object):
    def containsDuplicate(self, nums:List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        #khởi tạo mảng seen lưu giá trị không trùng lặp với pwhong thức set()
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
