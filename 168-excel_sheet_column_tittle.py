class Solution(object):
    def convertToTitle(self, columnNumber: int) -> str:
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""

        while columnNumber > 0:
            # Tính toán phần dư khi chia cho 26
            remainder = (columnNumber - 1) % 26
            # Chuyển đổi phần dư thành ký tự ASCII và thêm vào đầu chuỗi kết quả
            result = chr(ord('A') + remainder) + result
            # Cập nhật columnNumber bằng phần nguyên khi chia cho 26
            columnNumber = (columnNumber - 1) // 26
        return result
