import itertools


class Solution(object):
    def reformat(self, s:str)-> str:
        """
        Input: s = "a0b1c2"
        Output: "0a1b2c"
        Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
        """
        alpha = []
        digit = []
        res = []
        for char in s:
            if char.isalpha():
                alpha.append(char)
            elif char.isdigit():
                digit.append(digit)
        if abs(len(alpha)-len(digit)) > 1:
            return ''
        elif abs(len(alpha)-len(digit)) == 0:
            isDiffType = False
            for i in range(len(s)-1,0,-1):
                if s[i].isdigit() and s[i-1].isalpha() or s[i].isalpha() and s[i-1].isdigit():
                    isDiffType =True
            if isDiffType: return s

        longer_list = alpha if len(alpha) > len(digit) else digit
        shorter_list = alpha if len(alpha) < len(digit) else digit

        for alp, dig in zip(longer_list, shorter_list + ['']):
            res.append(alp)
            res.append(dig)

        return ''.join(res)