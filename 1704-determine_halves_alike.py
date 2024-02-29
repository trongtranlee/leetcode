class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def countVowels(string):
            vowels = set('aeiouAEIOU')
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            return count

        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]

        vowels_a = countVowels(a)
        vowels_b = countVowels(b)

        return vowels_a == vowels_b