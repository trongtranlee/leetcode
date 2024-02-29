class Solution(object):
    def numWaterBottles(self, numBottles:int, numExchange:int)-> int:
        """
        Input: numBottles = 9, numExchange = 3
        Output: 13
        Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
        Number of water bottles you can drink: 9 + 3 + 1 = 13.
        """
        drink = 0
        numEmpty = 0
        while numBottles > 0:
            drink = drink + numBottles
            numEmpty = numEmpty + numBottles
            numBottles = numEmpty // numExchange
            numEmpty = numEmpty - (numBottles * numExchange)
        return drink
