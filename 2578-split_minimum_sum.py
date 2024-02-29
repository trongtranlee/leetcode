from queue import PriorityQueue


class Solution(object):
    def splitNum(self, num:int)-> int:
        """
        :type num: int
        :rtype: int
        """
        fn, sn = '', ''
        num = str(num)
        num = sorted(num)

        for idx, num in enumerate(num):
            if idx % 2:
                fn += num
            else:
                sn += num
        if fn == '':
            fn = 0
        if sn == '':
            sn = 0
        return (int(fn) + int(sn))
