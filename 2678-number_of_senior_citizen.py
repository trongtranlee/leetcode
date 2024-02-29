class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        return sum(int(detail[11:13]) > 60 for detail in details)