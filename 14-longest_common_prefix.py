from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs:List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Initialize the longest common prefix as the first string
        longest_prefix = strs[0]

        # Iterate through the remaining strings
        for s in strs[1:]:
            # Compare each character of the current string with the longest common prefix
            i = 0
            while i < len(longest_prefix) and i < len(s) and longest_prefix[i] == s[i]:
                i += 1

            # Update the longest common prefix to be the common prefix found so far
            longest_prefix = longest_prefix[:i]

            # If the longest common prefix becomes empty, no need to continue
            if not longest_prefix:
                break

        return longest_prefix
