class Solution(object):
    def checkRecord(self, s:str)-> bool:
        """
        :type s: str
        :rtype: bool
        """
        absent_count = 0
        late_streak = 0

        for char in s:
            if char == 'A':
                absent_count += 1
                if absent_count >= 2:
                    return False
                late_streak = 0
            elif char == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:  # char == 'P'
                late_streak = 0

        return True
