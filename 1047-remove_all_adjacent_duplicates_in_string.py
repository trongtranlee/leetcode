class Solution(object):
    def removeDuplicates(self, s:str)-> str:
        """
        :type s: str
        :rtype: str
        Input: s = "azxxzy"
        Output: "ay"
        """

        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
