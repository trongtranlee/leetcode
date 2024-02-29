class Solution(object):
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Input: text = "hello world", brokenLetters = "ad"
        Output: 1
        Explanation: We cannot type "world" because the 'd' key is broken.
        """
        words = text.split()
        max_words = len(words)
        for word in words:
            for char in brokenLetters:
                if char in word:
                    max_words -=1
                    break
        return max_words

