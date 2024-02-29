from typing import List


class Solution(object):
    def relativeSortArray(self, arr1:List[int], arr2:List[int])-> List[int]:
        """
        Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
        Output: [22,28,8,6,17,44]
        """
        diff = []
        for i in arr1:
            if i not in arr2:
                diff.append(i)
        diff.sort()
        res = []
        for num2 in arr2:
            for num1 in arr1:
                if num1 == num2:
                    res.append(num1)

        for i in diff:
            res.append(i)

        return res

