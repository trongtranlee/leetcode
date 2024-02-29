class Solution(object):
    def isPathCrossing(self, path:str)-> bool:
        """
        Input: path = "NES"
        Output: false
        Explanation: Notice that the path doesn't cross any point more than once.
        """
        y = 0
        x = 0
        seen = {(0, 0)}
        for letter in path:
            print(x, y, letter)
            if letter == 'N':
                y += 1
            if letter == 'S':
                y -= 1
            if letter == 'E':
                x += 1
            if letter == 'W':
                x -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False

