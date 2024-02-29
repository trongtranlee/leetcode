class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count = 0

        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1

        return count