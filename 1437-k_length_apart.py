from typing import List

class Solution(object):
    def kLengthApart(self, nums:List[int], k:int)-> bool:
        """
        Input: nums = [1,0,0,0,1,0,0,1], k = 2
        Output: true
        Explanation: Each of the 1s are at least 2 places away from each other.
        """
        distance = k

        for num in nums:
            if num == 1:
                if distance < k:
                    return False
                distance = 0
            else:
                distance += 1

        return True


