from collections import Counter


class Solution(object):
    def sortString(self, s:str)-> str:
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        result = []

        while counter:
            # Step 1: Pick the smallest character and append it to the result
            for char in sorted(counter):
                if counter[char] > 0:
                    result.append(char)
                    counter[char] -= 1
                    break

            # Step 2: Pick the smallest character greater than the last appended character
            for char in sorted(counter):
                if counter[char] > 0 and char > result[-1]:
                    result.append(char)
                    counter[char] -= 1
                    break

            # Step 5: Pick the largest character smaller than the last appended character
            for char in sorted(counter, reverse=True):
                if counter[char] > 0 and char < result[-1]:
                    result.append(char)
                    counter[char] -= 1
                    break

            # Step 6: Pick the largest character and append it to the result
            for char in sorted(counter, reverse=True):
                if counter[char] > 0:
                    result.append(char)
                    counter[char] -= 1
                    break

        return ''.join(result)
