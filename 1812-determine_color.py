class Solution(object):
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        :type coordinates: str
        :rtype: bool
        Input: coordinates = "a1"
        Output: false
        Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
        """
        letter = coordinates[0]
        number = int(coordinates[1])

        if (letter in 'aceg') == (number % 2 == 0):
            return True
        else:
            return False

