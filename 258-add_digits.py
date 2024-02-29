class Solution(object):
    def addDigits(self, num: int)-> int:
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        for i in str(num):
            sum += int(i)
        if sum >= 10:
            return self.addDigits(sum)
        else:
            return sum


