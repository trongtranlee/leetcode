from typing import List


class Solution(object):
    def arrayRankTransform(self, arr:List[int])-> List[int]:
        """
        Input: arr = [40,10,20,30]
        sortArr = [1:10,2:20,3:30,4:40]
        Output: [4,1,2,3]
        Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
        """
        sorted_arr = sorted(set(arr))
        rank_dict = {}
        rank = 1
        for value in sorted_arr:
            rank_dict[value] = rank
            rank += 1

        ranks = []
        for value in arr:
            rank = rank_dict[value]
            ranks.append(rank)

        #ranks = [rank_dict[value] for value in arr]

        return ranks





