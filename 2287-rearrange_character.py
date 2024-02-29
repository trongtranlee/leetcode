class Solution(object):
    def rearrangeCharacters(self, s:str, target:str)-> int:
        """
        Input: s = "ilovecodingonleetcode", target = "code"
        Output: 2
        Explanation:
        For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
        For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
        The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
        We can make at most two copies of "code", so we return 2.
        """
        max_copy = float('inf')
        hashtable = {}
        for char in target:
            hashtable[char] = hashtable.get(char, 0) + 1

        for char, freg in hashtable.items():
            if char not in s:
                return 0
            else:
                max_copy = min(max_copy, s.count(char) // freg)
        return max_copy



