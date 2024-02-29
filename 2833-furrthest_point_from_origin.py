class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l = 0
        r = 0
        u = 0
        for move in moves:
            if move == 'L':
                l += 1
            elif move == 'R':
                r += 1
            else:
                u += 1
        diff = l - r
        if diff < 0:
            diff = diff * -1

        return diff + u
