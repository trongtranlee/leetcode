class Solution(object):
    def dayOfYear(self, date:str)-> int:
        """
        :type date: str
        :rtype: int
        Input: date = "2019-02-10"
        Output: 41
        """
        year, month, day = map(int, date.split('-'))

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = sum(days_in_month[:month]) + day

        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            total_days += 1

        return total_days
