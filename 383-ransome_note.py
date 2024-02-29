from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote:str, magazine:str)-> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #Đếm số lần xuất hiện từng char trong 2 chuỗi
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)

        #Cho s1 giao s2 (&) trả về true nếu = s1 và false nếu ngược lại
        return s1 & s2 == s1
