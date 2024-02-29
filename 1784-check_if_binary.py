class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = False
        for i in range(1, len(s)):
            if s[i] == "0":
                check = True
            else:
                if check: return False
        return True