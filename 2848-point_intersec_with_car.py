class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        x = []
        count = 0
        for i in range(len(nums)):
            x1 = nums[i][0]
            x2 = nums[i][1]
            for j in range(x1, x2 + 1):
                if j in x:
                    pass
                if j not in x:
                    x.append(j)
                    count += 1
        return count
