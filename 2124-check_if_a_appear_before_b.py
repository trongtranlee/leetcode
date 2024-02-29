class Solution(object):
    def checkString(self, s:str)-> bool:
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
            if s[i] == "a" and s[i-1] == "b":
                return False
        return True
