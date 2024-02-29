class Solution(object):
    def maxPower(self, s:str)-> int:
        """
        Input: s = "leetcode"
        Output: 2
        Explanation: The substring "ee" is of length 2 with the character 'e' only.
        """
        max_len = 0
        curr_len = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1

        max_len = max(max_len, curr_len)

        return max_len
