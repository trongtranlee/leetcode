from astroid import List


class Solution(object):
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right + 1):
            if '0' in str(i):
                continue
            is_self_dividing = True
            for char in str(i):
                if i % int(char) != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                result.append(i)
        return result

