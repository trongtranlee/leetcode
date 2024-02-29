from collections import Counter


class Solution(object):
    def firstUniqChar(self, s:str)->int:
        """
        :type s: str
        :rtype: int
        """
        #Đếm số lần xuất hiện từng char và lưu vào s_counter
        s_counter = Counter(s)
        for i, char in enumerate(s):
            if s_counter[char] == 1:
                return i
        return -1
