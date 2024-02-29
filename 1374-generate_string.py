class Solution(object):
    def generateTheString(self, n:int)->str:
        """
        Input: n = 4
        Output: "pppz"
        Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once.
        Note that there are many other valid strings such as "ohhh" and "love".
        """
        res = ''
        if n % 2 != 0:
            for i in range(n):
                res += "x"
        else:
            for i in range(n-1):
                res += "x"
            res += "y"
        return res


