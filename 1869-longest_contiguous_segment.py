class Solution(object):
    def checkZeroOnes(self, s:str)-> bool:
        """
        Input: s = "1101"
        Output: true
        Explanation:
        The longest contiguous segment of 1s has length 2: "1101"
        The longest contiguous segment of 0s has length 1: "1101"
        The segment of 1s is longer, so return true.
        """
        max_length_1 = 0
        max_length_0 = 0
        count_1 = 0
        count_0 = 0
        for digit in s:
            if digit == "1":
                count_1 += 1
                max_length_1 = max(count_1, max_length_1)
                count_0 = 0
            else:
                count_0 += 1
                max_length_0 = max(count_0, max_length_0)
                count_1 = 0  

        return max_length_1 > max_length_0
