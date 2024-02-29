from typing import List


class Solution(object):
    def findClosestNumber(self, nums:List[int])-> int:
        """
        Input: nums = [-4,-2,1,4,8]
        Output: 1
        Explanation:
        The distance from -4 to 0 is |-4| = 4.
        The distance from -2 to 0 is |-2| = 2.
        The distance from 1 to 0 is |1| = 1.
        The distance from 4 to 0 is |4| = 4.
        The distance from 8 to 0 is |8| = 8.
        Thus, the closest number to 0 in the array is 1.
        """
        closest_num = float('inf')
        closest_abs = float('inf')

        for num in nums:
            abs_num = abs(num)
            if abs_num < closest_abs or (abs_num == closest_abs and num > closest_num):
                closest_num = num
                closest_abs = abs_num

        return closest_num

