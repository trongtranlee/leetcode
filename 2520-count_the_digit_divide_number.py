class Solution(object):
    def countDigits(self, num:int)-> int:
        """
        Input: num = 121
        Output: 2
        Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
        """
        count  = 0
        for digit in str(num):
            if num % int(digit) == 0:
                count +=1
        return count
