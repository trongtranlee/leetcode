from typing import List

class Solution(object):
    def numOfStrings(self, patterns:List[str], word:str)-> int:
        """
        Input: patterns = ["a","abc","bc","d"], word = "abc"
        Output: 3
        Explanation:
        - "a" appears as a substring in "abc".
        - "abc" appears as a substring in "abc".
        - "bc" appears as a substring in "abc".
        - "d" does not appear as a substring in "abc".
        3 of the strings in patterns appear as a substring in word.
        """
        count = 0
        for string in patterns:
            if string in word:
                count +=1
        return count
