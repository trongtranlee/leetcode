from astroid import List


class Solution(object):
    def nextGreatestLetter(self, letters: List[str], target:str)-> str:
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(0, len(letters)):
            if letters[i] > target:
                return letters[i]
                break

        return letters[0]

