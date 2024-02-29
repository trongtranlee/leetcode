from typing import List


class Solution(object):
    def countWords(self, words1:List[str], words2:List[str])-> int:
        """
        Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
        Output: 2
        Explanation:
        - "leetcode" appears exactly once in each of the two arrays. We count this string.
        - "amazing" appears exactly once in each of the two arrays. We count this string.
        """
        counts1 = {}
        counts2 = {}
        for word in words1:
            counts1[word] = words1.count(word)

        for word in words2:
            counts2[word] = words2.count(word)

        count = 0
        for word, freq1 in counts1.items():
            if freq1 == 1 and word in counts2:
                count += 1

        for word, freq2 in counts2.items():
            if freq2 == 1 and word in counts1:
                count += 1
        return count//2