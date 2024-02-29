class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky = False
        product = length * width * height
        if length >= 10000 or width >= 10000 or height >= 10000 or product >= 1000000000:
            bulky = True
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky:
            return "Bulky"
        else:
            return "Heavy"
