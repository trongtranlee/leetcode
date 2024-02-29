from collections import Counter

from astroid import List


class Solution(object):
    def largeGroupPositions(self, s:str)-> List[List[int]]:
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0

        # Iterate through the string
        for i in range(len(s)):
            # Check if the current character is different from the next character or if it's the last character
            if i == len(s) - 1 or s[i] != s[i + 1]:
                # Calculate the length of the current group
                length = i - start + 1
                # Check if the group is large
                if length >= 3:
                    # Add the interval of the large group to the result
                    result.append([start, i])
                # Update the start index for the next group
                start = i + 1

        return result