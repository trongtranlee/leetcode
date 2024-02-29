class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        Input: sequence = "ababc", word = "ab"
        Output: 2
        Explanation: "abab" is a substring in "ababc".
        """
        max_k = 0
        len_word = len(word)
        for i in range(len(sequence)):
            k = 0
            j = i
            while sequence[j:j + len_word] == word:
                k += 1
                j += len_word

            # Update max_k if k is greater
            max_k = max(max_k, k)

        return max_k
