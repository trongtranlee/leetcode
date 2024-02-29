from typing import List


class Solution(object):
    def mostFrequentEven(self, nums:List[int])-> int:
        """
        Input: nums = [0,1,2,2,4,4,1]
        Output: 2
        Explanation:
        The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
        We return the smallest one, which is 2.
        """
        count = {}
        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1

        most_frequent = -1
        max_count = 0
        for num, freq in count.items():
            if freq > max_count or (freq == max_count and num < most_frequent):
                most_frequent = num
                max_count = freq

        return most_frequent

