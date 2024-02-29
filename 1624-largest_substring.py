class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Input: s = "abca"
        Output: 2
        Explanation: The optimal substring here is "bc".
        """
        char_indices = {}
        max_length = -1

        for i, char in enumerate(s):
            if char in char_indices:
                max_length = max(max_length, i - char_indices[char] - 1)
            else:
                char_indices[char] = i

        return max_length if max_length != -1 else -1
