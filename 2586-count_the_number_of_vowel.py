from typing import List


class Solution(object):
    def vowelStrings(self, words:List[str], left:int, right:int)-> int:
        """
        Input: words = ["are","amy","u"], left = 0, right = 2
        Output: 2
        Explanation:
        - "are" is a vowel string because it starts with 'a' and ends with 'e'.
        - "amy" is not a vowel string because it does not end with a vowel.
        - "u" is a vowel string because it starts with 'u' and ends with 'u'.
        The number of vowel strings in the mentioned range is 2.
        """
        v = 'aeiou'
        count = 0
        x = words[left:right + 1]
        for i in x:
            if i[0] in v and i[len(i) - 1] in v:
                count += 1
        return count

