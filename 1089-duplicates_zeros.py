from typing import List


class Solution(object):
    def duplicateZeros(self, arr: List[int]):
        """
        Input: arr = [1,0,2,3,0,4,5,0]
        Output: [1,0,0,2,3,0,0,4]
        Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
        """
        n = len(arr)
        zeroes = arr.count(0)
        total_length = n + zeroes
        new_arr = [0] * total_length  # Create a new list with the required length
        index = 0
        for i in range(n):
            if arr[i] == 0:
                new_arr[index] = 0
                index += 1
                if index < total_length:  # Check if index is within the range
                    new_arr[index] = 0
            else:
                new_arr[index] = arr[i]
            index += 1

        # Copy elements from new_arr back to arr
        for i in range(n):
            arr[i] = new_arr[i]