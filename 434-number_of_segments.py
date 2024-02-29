class Solution(object):
    def countSegments(self, s:str)-> int:
        """
        :type s: str
        :rtype: int
        """
        result = s.split()
        return len(result)
