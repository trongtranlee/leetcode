from datetime import datetime, date


class Solution(object):
    def dayOfTheWeek(self, day:int, month:int, year:int)-> str:
        """
        Input: day = 31, month = 8, year = 2019
        Output: "Saturday"
        """
        return date(year, month, day).strftime("%A")

