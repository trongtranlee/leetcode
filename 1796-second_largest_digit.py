class Solution(object):
    def secondHighest(self, s:str)-> int:
        """
        Input: s = "dfa12321afd"
        Output: 2
        Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
        """
        digit_list = []
        for char in s:
            if char.isdigit():
                digit_list.append(int(char))
        digit_set = set(digit_list)

        if len(digit_set) < 2:
            return -1
        else:
            digit_list = sorted(digit_set, reverse=True) 
            return digit_list[1]
