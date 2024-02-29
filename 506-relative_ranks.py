from typing import List


class Solution(object):
    def findRelativeRanks(self, score:List[int])-> List[int]:
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Sắp xếp mảng điểm số giảm dần
        sorted_score = sorted(score, reverse=True)

        # Tạo một từ điển ánh xạ từ điểm số sang xếp hạng
        rank_dict = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                rank_dict[s] = "Gold Medal"
            elif i == 1:
                rank_dict[s] = "Silver Medal"
            elif i == 2:
                rank_dict[s] = "Bronze Medal"
            else:
                rank_dict[s] = str(i + 1)

        # Ánh xạ xếp hạng của từng vận động viên từ từ điển
        return [rank_dict[score] for score in score]

