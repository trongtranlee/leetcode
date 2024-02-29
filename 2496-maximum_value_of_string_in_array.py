from typing import List


class Solution(object):
    def maximumValue(self, strs:List[str])-> int:
        """
        Input: strs = ["alic3","bob","3","4","00000"]
        Output: 5
        Explanation:
        - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
        - "bob" consists only of letters, so its value is also its length, i.e. 3.
        - "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
        - "4" also consists only of digits, so its value is 4.
        - "00000" consists only of digits, so its value is 0.
        Hence, the maximum value is 5, of "alic3".
        """

        max_value = 0
        for string in strs:
            if string.isdigit():
                max_value = max(max_value, int(string))
            else:
                max_value = max(max_value, len(string))
        return max_value
