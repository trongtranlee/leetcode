class Solution(object):
    def licenseKeyFormatting(self, s:str, k:int)-> str:
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Remove dashes and convert lowercase letters to uppercase
        s = s.replace('-', '').upper()
        # Calculate the length of the first group
        first_group_length = len(s) % k
        # Initialize the result string with the first group
        result = s[:first_group_length] + '-' if first_group_length > 0 else ''
        # Iterate over the remaining characters and add dashes
        for i in range(first_group_length, len(s), k):
            result += s[i:i + k] + '-'
        # Remove the trailing dash and return the result
        return result[:-1]