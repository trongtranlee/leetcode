from typing import List


class Solution(object):
    def stringMatching(self, words:List[str])-> List[str]:
        """
        Input: words = ["mass","as","hero","superhero"]
        Output: ["as","hero"]
        Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
        ["hero","as"] is also a valid answer.
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[j] in words[i] and len(words[j]) < len(words[i]) :
                    res.append(words[j])
        return set(res)

