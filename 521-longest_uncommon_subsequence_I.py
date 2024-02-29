class Solution(object):
    def findLUSlength(self, a:str, b:str)-> int:
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

