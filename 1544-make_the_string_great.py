class Solution(object):
    def makeGood(self, s:str)-> str:
        """
        Input: s = "abBAcC"
        Output: ""
        Explanation: We have many possible scenarios, and all lead to the same answer. For example:
        "abBAcC" --> "aAcC" --> "cC" --> ""
        "abBAcC" --> "abBA" --> "aA" --> ""
        """
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
