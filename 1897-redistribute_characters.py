
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        length = len(words)
        if length < 2:
            return True

        alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z']

        words = "".join(words)
        for alphabet in alphabet_list:
            if alphabet in words and words.count(alphabet) % length != 0:
                return False
        return True