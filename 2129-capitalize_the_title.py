class Solution(object):
    def capitalizeTitle(self, title:str)-> str:
        """
        :type title: str
        :rtype: str
        """
        words = title.split()

        capitalized_words = []
        for word in words:
            if len(word) <= 2:
                capitalized_words.append(word.lower())
            else:
                capitalized_words.append(word[0].upper() + word[1:].lower())

        return ' '.join(capitalized_words)

