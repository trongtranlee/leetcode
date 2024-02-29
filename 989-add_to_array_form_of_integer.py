from astroid import List


class Solution(object):
    def addToArrayForm(self, num:List[int], k:int)->List[int]:
        """
        Input: num = [1,2,0,0], k = 34
        Output: [1,2,3,4]
        Explanation: 1200 + 34 = 1234
        """
        # digit = num.Split()
        # strNum = ''.join(digit)
        # intNum = int(strNum) + k
        # result = []
        # for i in str(intNum):
        #     result.append(i)
        # return result

        total = 0
        n = len(num)
        for digit in num:
            total += digit * (10 ** (n - 1))
            n -= 1
        intRes = total + k
        res = []
        for i in str(intRes):
            res.append(int(i))
        return res


