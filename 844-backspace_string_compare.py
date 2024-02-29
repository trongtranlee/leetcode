class Solution(object):
    def backspaceCompare(self, s:str, t:str)-> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sResult = []
        tResult = []
        for char in s:
            if char != "#":
                sResult.append(char)
            elif sResult:
                sResult.pop()
        for char in t:
            if char != "#":
                tResult.append(char)
            elif tResult:
                tResult.pop()

        return sResult == tResult

