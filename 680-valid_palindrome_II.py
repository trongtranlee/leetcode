from collections import Counter


class Solution(object):
    def validPalindrome(self, s:str)-> bool:
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Check if the string becomes palindrome by deleting either left or right character
                return (s[left + 1:right + 1] == s[left + 1:right + 1][::-1]) or (s[left:right] == s[left:right][::-1])
            left += 1
            right -= 1

        return True

