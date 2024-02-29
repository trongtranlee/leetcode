from typing import List


class Solution(object):
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Input: arr = [1,2,34,3,4,5,7,23,12]
        Output: true
        Explanation: [5,7,23] are three consecutive odds.
        """
        count = 0
        for num in arr:
            if num % 2 != 0:
                count +=1
                if count == 3:
                    return True
            else:
                count = 0
        return False
