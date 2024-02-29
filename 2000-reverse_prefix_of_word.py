class Solution(object):
    def reversePrefix(self, word:str, ch:str)-> str:
        """
        Input: word = "abcdefd", ch = "d"
        Output: "dcbaefd"
        Explanation: The first occurrence of "d" is at index 3.
        Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
        """
        if ch not in word:
            return word
        res = []
        for i in range(len(word)):
            if word[i] != ch[0]:
                res.append(word[i])
            else:
                res.append(word[i])
                res.reverse()
                res.extend(word[i+1:])
                return ''.join(res)
