class Solution(object):
    def removeTrailingZeros(self, num:str)-> str:
        """
        :type num: str
        :rtype: str
        """
        return num.rstrip('0')
