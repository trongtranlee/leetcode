class Solution(object):
    def divisorSubstrings(self, num:int, k:int)-> int:
        """
        Input: num = 240, k = 2
        Output: 2
        Explanation: The following are the substrings of num of length k:
        - "24" from "240": 24 is a divisor of 240.
        - "40" from "240": 40 is a divisor of 240.
        Therefore, the k-beauty is 2.
        """
        count = 0
        str_num = str(num)
        for i in range(len(str_num) - k + 1):
            if int(str_num[i:i + k]) != 0 and num % int(str_num[i:i + k]) == 0:
                count += 1
        return count


