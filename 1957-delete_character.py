class Solution(object):
    def makeFancyString(self, s:str)-> str:
        """
        Input: s = "leeetcode"
        Output: "leetcode"
        Explanation:
        Remove an 'e' from the first group of 'e's to create "leetcode".
        No three consecutive characters are equal, so return "leetcode".
        """
        stack = []
        for i in range(len(s)):
            if len(stack) >= 2 and s[i] == stack[-1] == stack[-2]:
                continue
            else:
                stack.append(s[i])
        return ''.join(stack)

