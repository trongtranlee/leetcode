from astroid import List


class Solution(object):
    def isAlienSorted(self, words:List[str], order:str)->bool:
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alien_order = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]

                if char1 != char2:
                    if alien_order[char1] > alien_order[char2]:
                        return False
                    break
            if len(word1) > len(word2):
                return False

        return True