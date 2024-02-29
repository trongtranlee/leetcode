class Solution(object):
    def areNumbersAscending(self, s:str)-> bool:
        """
        Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
        Output: true
        Explanation: The numbers in s are: 1, 3, 4, 6, 12.
        They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
        """
        tokens = s.split()
        prev_number = None

        for token in tokens:
            if token.isdigit():
                current_number = int(token)
                if prev_number is not None and current_number <= prev_number:
                    return False
                prev_number = current_number

        return True

