class Solution(object):
    def thousandSeparator(self, n:int)-> str:
        """
        Input: n = 1234
        Output: "1.234"
        """
        str_n = str(n)
        if len(str_n) < 4:
            return str_n
        result = []
        for i in range(len(str_n)):
            if i > 0 and (len(str_n) - i) % 3 == 0:
                result.append('.')
            result.append(str_n[i])

        return ''.join(result)

