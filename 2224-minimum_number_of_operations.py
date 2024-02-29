class Solution(object):
    def convertTime(self, current:str, correct:str)-> int:
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        current_time = 60 * int(current[0:2]) + int(current[3:5])
        target_time = 60 * int(correct[0:2]) + int(correct[3:5])
        diff = target_time - current_time
        count = 0
        for i in [60, 15, 5, 1]:
            count += diff
            diff %= i  
        return count
