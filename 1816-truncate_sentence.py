class Solution(object):
    def truncateSentence(self, s:str, k:int)-> str:
        """
        Input: s = "Hello how are you Contestant", k = 4
        Output: "Hello how are you"
        Explanation:
        The words in s are ["Hello", "how" "are", "you", "Contestant"].
        The first 4 words are ["Hello", "how", "are", "you"].
        Hence, you should return "Hello how are you".
        """
        words = s.split()[:k]
        return ' '.join(words)
