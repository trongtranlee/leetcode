from astroid import List


class Solution(object):
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1Split = s1.split()
        s2Split = s2.split()
        result = []
        for i in s1Split:
            if i not in s2Split and s1Split.count(i) == 1:
                result.append(i)
        for j in s2Split:
            if j not in s1Split and s2Split.count(j) == 1:
                result.append(j)
        return result
