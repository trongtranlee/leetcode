class Solution(object):
    def freqAlphabets(self, s:str)-> str:
        """
        Characters ('a' to 'i') are represented by ('1' to '9') respectively.
        Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
        Input: s = "10#11#12"
        Output: "jkab"
        Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
        """
        mapping = {
            'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
            'j#': '10', 'k#': '11', 'l#': '12', 'm#': '13', 'n#': '14', 'o#': '15', 'p#': '16', 'q#': '17', 'r#': '18',
            's#': '19', 't#': '20', 'u#': '21', 'v#': '22', 'w#': '23', 'x#': '24', 'y#': '25', 'z#': '26'
        }
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result += mapping[s[i:i + 3]]
                i += 3
            else:
                result += mapping[s[i]]
                i += 1

        return result



