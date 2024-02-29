class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            for i in word.split(separator):
                if i:
                    ans.append(i)
        return ans
