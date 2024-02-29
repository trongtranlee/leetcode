from astroid import List


class Solution(object):
    def commonChars(self, words:List[str])->List[str]:
        """
        Input: words = ["cool","lock","cook"]
        Output: ["c","o"]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        word_sets = [set(word) for word in words]

        # Take the intersection of all sets
        common_chars = set.intersection(*word_sets)

        return list(common_chars)
