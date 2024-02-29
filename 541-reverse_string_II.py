class Solution(object):
    def reverseStr(self, s:str, k:int)-> str:
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        i = 0
        while i < len(s):
            # Đảo ngược ký tự đầu tiên trong mỗi phần 2k ký tự
            result += s[i:i + k][::-1]
            # Giữ nguyên phần còn lại của phần 2k ký tự nếu có
            result += s[i + k:i + 2 * k]
            # Di chuyển đến vị trí tiếp theo
            i += 2 * k
        return result
