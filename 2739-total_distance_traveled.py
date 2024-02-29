class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        mil = 0
        while mainTank != 0:
            if additionalTank == 0 and mainTank == 0:
                return mil
            if mainTank >= 5 and additionalTank >= 1:
                mainTank -= 5 - 1
                additionalTank -= 1
                mil += 5 * 10
            else:
                mil += mainTank * 10
                mainTank = 0

        return mil
