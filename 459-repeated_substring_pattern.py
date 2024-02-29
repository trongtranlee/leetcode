class Solution(object):
    def repeatedSubstringPattern(self, s:str)-> bool:
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        # Kiểm tra tất cả các độ dài của chuỗi con từ 1 đến n//2
        for i in range(1, n // 2 + 1):
            # Nếu độ dài chuỗi không chia hết cho i, thì chúng ta không cần kiểm tra
            if n % i != 0:
                continue
            # Lấy chuỗi con đầu tiên có độ dài i
            substr = s[:i]
            # Kiểm tra xem có tạo thành chuỗi ban đầu bằng cách nối nhiều bản sao của chuỗi con không
            if substr * (n // i) == s:
                return True
        return False
