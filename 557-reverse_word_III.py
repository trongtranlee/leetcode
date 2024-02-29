class Solution(object):
    def reverseWords(self, s:str)->str:
        """
        :type s: str
        :rtype: str
        """
        sSplit = s.split()
        for i in range(len(sSplit)):
            left = 0
            right = len(sSplit[i])-1
            word = list(sSplit[i])
            while left < right:
                word[left], word[right] = word[right], word[left]
                left +=1
                right -= 1
            sSplit[i] = ''.join(word)
        return ' '.join(sSplit)


