class Solution(object):
    def largestGoodInteger(self, num: str) -> str:
        """
        Input: num = "6777133339"
        Output: "777"
        Explanation: There are two distinct good integers: "777" and "333".
        "777" is the largest, so we return "777".
        """
        max_good = ""
        n = len(num)

        for i in range(n - 2):
            substring = num[i:i + 3]
            if len(set(substring)) == 1:
                max_good = max(max_good, substring)
        return max_good


