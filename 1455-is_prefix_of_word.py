class Solution(object):
    def isPrefixOfWord(self, sentence:str, searchWord:str)-> int:
        """
        Input: sentence = "i love eating burger", searchWord = "burg"
        Output: 4
        Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
        """
        words = sentence.split()
        for index, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return index
        return -1

