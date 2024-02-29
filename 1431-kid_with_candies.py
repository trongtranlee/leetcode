class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        Input: candies = [4,2,1,1,2], extraCandies = 1
        Output: [true,false,false,false,false]
        Explanation: There is only 1 extra candy.
        Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
        """
        res = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
