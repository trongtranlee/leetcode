# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

def guess(mid):
    pass


class Solution(object):
    def guessNumber(self, n:int)-> int:
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

        # Đoạn code này sẽ không được thực thi vì giả sử rằng luôn tồn tại một số mà bạn cần đoán.
        # Trong trường hợp này, nếu có lỗi xảy ra, ta sẽ trả về -1.
        return -1
