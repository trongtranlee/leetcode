class Solution(object):
    def maximum69Number(self, num:int)-> int:

        """
        Input: num = 9669
        Output: 9969
        Explanation:
        Changing the first digit results in 6669.
        Changing the second digit results in 9969.
        Changing the third digit results in 9699.
        Changing the fourth digit results in 9666.
        The maximum number is 9969.
        """
        str_num = str(num)
        if "6" not in str_num:
            return num
        else:
            return int(str_num.replace("6", "9", 1))

