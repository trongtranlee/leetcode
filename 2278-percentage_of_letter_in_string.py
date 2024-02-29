class Solution(object):
    def percentageLetter(self, s:str, letter:str)-> int:
        """
        Input: s = "foobar", letter = "o"
        Output: 33
        Explanation:
        The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
        """
        return (s.count(letter)*100)//len(s)