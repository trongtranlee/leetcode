class Solution(object):
    def toHex(self, num:int)-> str:
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        # Xử lý trường hợp số âm: Chuyển đổi sang dạng bù hai
        if num < 0:
            num += 2 ** 32

        # Bảng chứa các ký tự thập lục phân
        hex_chars = "0123456789abcdef"
        result = ""

        while num > 0:
            # Lấy phần dư từ phép chia cho 16
            remainder = num % 16
            # Lấy ký tự thích hợp từ bảng thập lục phân
            result += hex_chars[remainder]
            # Thực hiện phép chia để tiếp tục tìm phần dư
            num //= 16

        # Đảo ngược chuỗi kết quả
        result = result[::-1]
        return result