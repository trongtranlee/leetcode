class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        """
        res = []
        max_length = float('-inf')
        if not s:
            return 0
        for char in s:
            if char not in res:
                res.append(char)
            else:
                max_length = max(len(res), max_length)
                res = []
                res.append(char)
        max_length = max(len(res), max_length)
        return max_length
