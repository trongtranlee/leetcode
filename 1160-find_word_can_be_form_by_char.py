from collections import Counter
from typing import List


class Solution(object):
    def countCharacters(self, words:List[str], chars:str)-> int:
        """
        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        """
        length = 0
        charsCounter = Counter(chars)

        for word in words:
            wordCounter = Counter(word)
            good_word = True
            word_length = 0

            for char, count in wordCounter.items():
                if char not in charsCounter or count > charsCounter[char]:
                    good_word = False
                    break
                else:
                    word_length += count

            if good_word:
                length += word_length

        return length


