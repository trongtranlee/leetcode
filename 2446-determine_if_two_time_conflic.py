from typing import List


class Solution(object):
    def haveConflict(self, event1:List[str], event2:List[str])-> bool:
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        start_time1, end_time1 = event1
        start_time2, end_time2 = event2

        start_minutes1 = int(start_time1[:2]) * 60 + int(start_time1[3:])
        end_minutes1 = int(end_time1[:2]) * 60 + int(end_time1[3:])
        start_minutes2 = int(start_time2[:2]) * 60 + int(start_time2[3:])
        end_minutes2 = int(end_time2[:2]) * 60 + int(end_time2[3:])

        if end_minutes1 < start_minutes2 or end_minutes2 < start_minutes1:
            return False
        else:
            return True