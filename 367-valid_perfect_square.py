class Solution(object):
    def isPerfectSquare(self, num:int)-> bool:
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

            # Kiểm tra từng số từ 1 đến căn bậc hai của num
        for i in range(1, int(num ** 0.5) + 1):
            if i * i == num:
                return True

        return False