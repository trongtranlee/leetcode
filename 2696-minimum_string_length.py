class Solution(object):
    def minLength(self, s:str)-> int:
        """
        Input: s = "ABFCACDB"
        Output: 2
        Explanation: We can do the following operations:
        - Remove the substring "ABFCACDB", so s = "FCACDB".
        - Remove the substring "FCACDB", so s = "FCAB".
        - Remove the substring "FCAB", so s = "FC".
        So the resulting length of the string is 2.
        It can be shown that it is the minimum length that we can obtain.
        """
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s = s.replace('AB', '')
            elif 'CD' in s:
                s = s.replace('CD', '')
        return len(s)