class Solution(object):
    def isSubsequence(self, s:str, t:str)-> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        curr = 0
        # Iterate through the characters of t
        for char in t:
            # If the current character in t matches the current character in s
            if s[curr] == char:
                curr += 1
                # If all characters in s are matched, return True
                if curr == len(s):
                    return True

        # If not all characters in s are matched, return False
        return False
