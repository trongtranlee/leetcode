class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches_played = 0

        while n > 1:
            if n % 2 == 0:
                matches_played += n // 2
                n //= 2
            else:
                matches_played += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return matches_played