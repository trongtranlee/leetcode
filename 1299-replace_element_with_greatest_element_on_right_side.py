from typing import List


class Solution(object):
    def replaceElements(self, arr:List[int])-> List[int]:
        """
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
        """
        for i in range(len(arr) - 1):
            if arr[i + 1:]:
                arr[i] = max(arr[i + 1:])
        arr[-1] = -1
        return arr
