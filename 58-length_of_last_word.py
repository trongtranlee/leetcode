import re
class Solution(object):
    def lengthOfLastWord(self, s:str) -> int:
        """
        :type s: str
        :rtype: int
        """
        words = re.findall(r'\b\w+\b', s)
        return len(words[-1])