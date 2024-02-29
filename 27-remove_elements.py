from typing import List


class Solution(object):
    def strStr(haystack: str, needle: str) -> int:
        x = len(needle)
        for i in range(0,len(haystack)):
            if haystack[i:i+x] == needle:
                return i
        return -1
