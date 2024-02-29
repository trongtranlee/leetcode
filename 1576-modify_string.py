class Solution(object):
    def modifyString(self, s:str)-> str:
        """
        Input: s = "ubv?w"
        Output: "ubvaw"
        Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the
        strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
        """
        string_clone = []
        left = 0
        right = len(s)-1
        while left < right:
            if left != "?" and right != "?":
                string_clone[left] = s[left]
                string_clone[right] = s[right]
                left +=1
                right -=1
            else:
                return 'Chưa nghĩ ra cách giải -.-'


