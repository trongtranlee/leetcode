from fractions import gcd

class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i, num in enumerate(nums):
            d = num % 10
            for j in range(i):
                n = nums[j]
                while n >= 10:
                    n //= 10
                ans += gcd(d, n) == 1
        return ans
