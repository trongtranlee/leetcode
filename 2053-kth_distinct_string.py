from typing import List


class Solution(object):
    def kthDistinct(self, arr:List[str], k:int)->str:
        """
        Input: arr = ["aaa","aa","a"], k = 1
        Output: "aaa"
        Explanation:
        All strings in arr are distinct, so the 1st string "aaa" is returned.
        """
        counts = {}

        for string in arr:
            counts[string] = counts.get(string, 0) + 1

        distinct_count = 0
        for string in arr:
            if counts[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string

        return ""
