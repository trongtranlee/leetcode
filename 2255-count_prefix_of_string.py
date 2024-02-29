from typing import List

class Solution(object):
    def countPrefixes(self, words:List[str], s:str)-> int:
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for strg in words:
            if s.startswith(strg):
                count +=1
        return count

