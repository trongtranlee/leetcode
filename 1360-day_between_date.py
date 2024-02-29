from datetime import datetime


class Solution(object):
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        a = datetime.strptime(date1, "%Y-%m-%d").date()
        b = datetime.strptime(date2, "%Y-%m-%d").date()
        mi = min(a, b)
        ma = max(a, b)
        return (ma - mi).days
