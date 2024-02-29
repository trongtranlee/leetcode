from typing import List


class Solution(object):
    def isPrefixString(self, s:str, words:List[str])-> bool:
        """
        Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
        Output: true
        Explanation:
        s can be made by concatenating "i", "love", and "leetcode" together.
        """
        concatenated = ''
        for word in words:
            concatenated += word
            if concatenated == s:
                return True
            elif len(concatenated) > len(s):
                return False
        return False