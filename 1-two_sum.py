from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Tạo hashmap rỗng để lưu key và value
        hashMap = {}

        #Duyệt mảng và gán giá trị tương ứng key.
        for index, value in enumerate(nums):
            otherValue = target - value

            #Ktra nếu tồn tại giá trị cần tìm trong map thì trả về
            if otherValue in hashMap:
                return [hashMap[otherValue], index]

            hashMap[value] = index
        return []
