class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = 0

        # Iterate through each rectangle
        for rectangle in rectangles:
            # Find the minimum side length of the current rectangle
            side_length = min(rectangle)
            # Update maxLen if the current side length is greater
            maxLen = max(maxLen, side_length)

        # Count the number of rectangles that can make a square with side length of maxLen
        count = 0
        for rectangle in rectangles:
            if min(rectangle) >= maxLen:
                count += 1

        return count
