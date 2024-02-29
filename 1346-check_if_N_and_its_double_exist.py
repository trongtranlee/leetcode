from typing import List


class Solution(object):
    def checkIfExist(self, arr: List[int])-> bool:
        """
        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]

        Input: arr = [10,2,5,3]
        Output: true
        Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
