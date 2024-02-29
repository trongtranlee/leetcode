from collections import Counter

from astroid import List


class Solution(object):
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.lower().split()
        valid_words = []
        for word in words:
            if word not in banned:
                valid_words.append(word)

        word_counts = Counter(valid_words)
        most_common_word = word_counts.most_common(1)[0][0]

        return most_common_word

