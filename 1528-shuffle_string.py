from typing import List


class Solution(object):
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
        Output: "leetcode"
        Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
        """
        res = [''] * len(s)
        for index, digit in enumerate(indices):
            res[digit] = s[index]
        return ''.join(res)
