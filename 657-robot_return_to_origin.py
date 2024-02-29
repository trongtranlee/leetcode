class Solution(object):
    def judgeCircle(self, moves:str)-> bool:
        """
        :type moves: str
        :rtype: bool
        """
        moveList = ['L','R', 'U','D']
        lCount = 0
        rCount = 0
        uCount = 0
        dCount = 0
        for i in moves:
            if i == moveList[0]:
                lCount += 1
            if i == moveList[1]:
                rCount += 1
            if i == moveList[2]:
                uCount += 1
            if i == moveList[3]:
                dCount += 1
        if lCount == rCount and uCount == dCount:
            return True
        return False


