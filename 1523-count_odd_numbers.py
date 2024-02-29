class Solution(object):
    def countOdds(self, low: int, high:int)-> int:
        """
        Input: low = 3, high = 7
        Output: 3
        Explanation: The odd numbers between 3 and 7 are [3,5,7].
        3 4 5 6 7 8 9
        """
        length = high - low
        if high % 2 == 0 and low % 2 ==0:
            return length // 2
        elif length % 2 != 0:
            return (length + 1) // 2
        else:
            return (length // 2) +1
