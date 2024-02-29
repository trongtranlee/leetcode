from collections import Counter


class Solution(object):
    def findTheDifference(self, s:str, t:str)-> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_counter = Counter(s)
        t_counter = Counter(t)

        # Subtract the counts of characters in s from those in t
        diff_counter = t_counter - s_counter

        # Return the character with positive count in the difference Counter
        for char, count in diff_counter.items():
            if count > 0:
                return char



