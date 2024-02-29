class Solution(object):
    def sortSentence(self, s:str)-> str:
        """
        Input: s = "is2 sentence4 This1 a3"
        Output: "This is a sentence"
        Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
        """
        s = s[::-1] #đảo ngược câu
        s = s.split()
        s = sorted(s)
        for i in range(len(s)):
            s[i] = s[i][:0:-1] #đảo ngược trừ ký tự đầu tiên
        return ' '.join(s)