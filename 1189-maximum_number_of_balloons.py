from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text:str)-> int:
        """
        Input: text = "loonbalxballpoon"
        Output: 2
        """
        balloonCounter = Counter('balloon')
        textCounter = Counter(text)

        for char, freq in balloonCounter.items():
            if char not in textCounter or textCounter[char] < freq:
                return 0

        max_instances = float('inf')
        for char, freq in balloonCounter.items():
            max_instances = min(max_instances, textCounter[char] // freq)

        return max_instances


