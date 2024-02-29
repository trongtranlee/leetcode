class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        Input: time = "2?:?0"
        Output: "23:50"
        Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
        """
        time = list(time)

        if time[0] == '?':
            time[0] = '2' if time[1] == '?' or int(time[1]) <= 3 else '1'

        if time[1] == '?':
            time[1] = '3' if time[0] == '2' else '9'

        if time[3] == '?':
            time[3] = '5'

        if time[4] == '?':
            time[4] = '9'

        return ''.join(time)
