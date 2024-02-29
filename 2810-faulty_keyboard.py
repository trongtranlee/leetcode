class Solution(object):
    def finalString(self, s:str)-> str:
        """
        Input: s = "string"
        Output: "rtsng"
        Explanation:
        After typing first character, the text on the screen is "s".
        After the second character, the text is "st".
        After the third character, the text is "str".
        Since the fourth character is an 'i', the text gets reversed and becomes "rts".
        After the fifth character, the text is "rtsn".
        After the sixth character, the text is "rtsng".
        Therefore, we return "rtsng".
        """
        res = ''
        for char in s:
            if char != "i":
                res += char
            else:
                res = res[::-1]
        return res

