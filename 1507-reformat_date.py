
class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        d, m, y = date.split(" ")
        d = "0" + d[0] if len(d) == 3 else d[:2]
        m = months.get(m)
        return y + "-" + m + "-" + d
