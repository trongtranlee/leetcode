from collections import Counter


class Solution(object):
    def longestPalindrome(self, s:str)-> int:
        """
        :type s: str
        :rtype: int
        """
        count = 0
        odd_count = 0
        sCount = Counter(s)
        for char in sCount:
            if sCount[char] % 2 == 0:
                count += sCount[char]
            if sCount[char] >= 3 and sCount[char] % 2 != 0:
                count = count + sCount[char] - 1
            if sCount[char] % 2 != 0:
                odd_count += 1
        if odd_count > 0:
            return count + 1
        else:
            return count