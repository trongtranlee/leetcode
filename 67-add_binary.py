class Solution(object):
    def addBinary(self, a: str, b:str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #Chuyển chuỗi về bin về kết quả int
        num1 = int(a, 2)
        num2 = int(b, 2)

        num = num1 + num2

        #Chuyển ngược lại int qua bin
        res = bin(num)

        #Loại bỏ tiền tố 0b của bin
        return res[2:]