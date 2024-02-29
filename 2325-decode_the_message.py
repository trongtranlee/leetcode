class Solution(object):
    def decodeMessage(self, key:str, message:str)-> str:
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        substitution_table = {}
        key_index = 0
        for char in key:
            if char.isalpha() and char.lower() not in substitution_table:
                substitution_table[char.lower()] = chr(ord('a') + key_index)
                key_index += 1

        for i in range(26):
            char = chr(ord('a') + i)
            if char not in substitution_table:
                substitution_table[char] = chr(ord('a') + key_index)
                key_index += 1

        decoded_message = ""
        for char in message:
            if char.isalpha():
                decoded_message += substitution_table[char.lower()]
            elif char == ' ':
                decoded_message += ' '

        return decoded_message

