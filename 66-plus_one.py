from typing import List


class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Trả về ngay sau khi cập nhật phần tử
            else:
                digits[i] = 0  # Đặt phần tử hiện tại thành 0 và tiếp tục với phần tử trước đó
        # Nếu hết vòng lặp mà vẫn chưa trả về, tức là tất cả các phần tử đều là 9
        # Thêm 1 vào đầu mảng và trả về
        return [1] + digits