from astroid import List


class Solution(object):
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        :type words: List[str]
        :rtype: int
        """
        morse_string = ""
        string_array = []
        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }

        for item in words:
            for char in item:
                if char.upper() in morse_code:
                    morse_string += morse_code[char.upper()] + ''
                else:
                    continue
            string_array.append(morse_string)
            morse_string = ''
        return len(set(string_array))





