class Solution(object):
    def maxScore(self, s:str)-> int:
        """
        Input: s = "011101"
        Output: 5
        Explanation:
        All possible ways of splitting s into two non-empty substrings are:
        left = "0" and right = "11101", score = 1 + 4 = 5
        left = "01" and right = "1101", score = 1 + 3 = 4
        left = "011" and right = "101", score = 1 + 2 = 3
        left = "0111" and right = "01", score = 1 + 1 = 2
        left = "01110" and right = "1", score = 2 + 1 = 3
        """
        max_score = 0
        zeros_count = 0
        ones_count = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_count += 1
            else:
                ones_count -= 1

            max_score = max(max_score, zeros_count + ones_count)

        return max_score
