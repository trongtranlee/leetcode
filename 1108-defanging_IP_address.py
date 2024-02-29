class Solution(object):
    def defangIPaddr(self, address:str)-> str:
        """
        :type address: str
        :rtype: str
        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"
        """
        res = []
        for i in address:
            if i == '.':
                res.append('[' + i + ']')
            else:
                res.append(i)
        return ''.join(res)

