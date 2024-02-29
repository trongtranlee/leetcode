class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        i = -1
        for x, y, z in zip(s1, s2, s3):
            if not x == y == z:
                break
            i += 1
        return (l1 - i - 1) + (l2 - i - 1) + (l3 - i - 1) if i != -1 else -1
