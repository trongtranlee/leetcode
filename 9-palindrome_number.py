class Solution(object):
    def isPalindrome(self, x:int) -> bool:
        """
        :type x: int
        :rtype: bool
        Vd: koolook
        """
        strX = str(x)
        for i in range(0, len(strX) / 2):
            if strX[i] != strX[len(strX) - i - 1]:
                return False
        return True

