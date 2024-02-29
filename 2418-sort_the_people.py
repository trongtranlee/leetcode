from typing import List


class Solution(object):
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Input: names = ["Mary","John","Emma"], heights = [180,165,170]
        Output: ["Mary","Emma","John"]
        Explanation: Mary is the tallest, followed by Emma and John.
        """
        list1 = []
        for i in range(len(names)):
            list1.append([heights[i], names[i]])
        list1.sort(reverse=True)
        list2 = []
        for i in range(len(names)):
            list2.append(list1[i][1])
        return list2


