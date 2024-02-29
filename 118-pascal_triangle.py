from typing import List


class Solution(object):
    def generate(self, numRows:int) ->List[List[int]] :
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        # Khởi tạo ma trận để lưu giá trị của tam giác Pascal
        triangle = [[1]]

        # Xây dựng tam giác Pascal
        for i in range(1, numRows):
            # Tạo một hàng mới của tam giác Pascal
            row = [1] * (i + 1)
            # Cập nhật giá trị của các phần tử ở giữa hàng mới
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            # Thêm hàng mới vào tam giác Pascal
            triangle.append(row)

        return triangle
