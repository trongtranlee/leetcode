class Solution(object):
    def minimumRecolors(self, blocks:str, k:int)-> int:
        """
        Input: blocks = "WBBWWBBWBW", k = 7
        Output: 3
        Explanation:
        One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
        so that blocks = "BBBBBBBWBW".
        It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
        Therefore, we return 3.
        """
        n = len(blocks)
        min_operations = float('inf')

        for i in range(n - k + 1):
            operations = 0
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    operations += 1
            min_operations = min(min_operations, operations)

        return min_operations

