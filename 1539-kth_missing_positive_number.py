from typing import List


class Solution(object):
    def findKthPositive(self, arr:List[int], k:int)-> int:
        """
        Input: arr = [2,3,4,7,11], k = 5
        Output: 9
        Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
        """
        miss_list = []
        for i in range(1,arr[-1]+k+1):
            if i not in arr:
                miss_list.append(i)
        return miss_list[k-1]
