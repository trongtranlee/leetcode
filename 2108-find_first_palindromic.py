from typing import List


class Solution(object):
    def firstPalindrome(self, words:List[str])-> str:
        """
        Input: words = ["abc","car","ada","racecar","cool"]
        Output: "ada"
        Explanation: The first string that is palindromic is "ada".
        Note that "racecar" is also palindromic, but it is not the first.
        """
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
        return ""

