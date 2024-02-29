from typing import List


class Solution(object):
    def canMakeArithmeticProgression(self, arr:List[int])-> bool:
        """
        Input: arr = [3,5,1]
        Output: true
        Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
        """
        arr.sort()
        diff = abs(arr[0]-arr[1])
        for i in range(len(arr)-1,0,-1):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
