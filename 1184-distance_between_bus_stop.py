from typing import List


class Solution(object):
    def distanceBetweenBusStops(self, distance:List[int], start:int, destination:int)-> int:
        """
        Input: distance = [1,2,3,4], start = 0, destination = 1
        Output: 1
        Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
        """
        if start > destination:
            start, destination = destination, start
        sumDis = sum(distance)
        clockSideDis = 0
        for i in range(start, destination):
            clockSideDis += distance[i]

        counterClockSideDis = sumDis - clockSideDis
        return min(clockSideDis, counterClockSideDis)




