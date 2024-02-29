class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime:int, delayedTime:int)-> int:
        """
        Input: arrivalTime = 15, delayedTime = 5
        Output: 20
        Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
        """
        ans = arrivalTime + delayedTime
        if ans < 24:
            return ans
        return ans - 24
