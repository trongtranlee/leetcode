class Solution(object):
    def isSameAfterReversals(self, num:int)-> bool:
        """
        :type num: int
        :rtype: bool
        """
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])
        return reversed2 == num


