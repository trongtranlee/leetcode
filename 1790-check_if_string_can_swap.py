class Solution(object):
    def areAlmostEqual(self, s1:str, s2:str)-> bool:
        """
        Input: s1 = "bank", s2 = "kanb"
        Output: true
        Explanation: For example, swap the first character with the last character of s2 to make "bank".
        """
        if s1 == s2:
            return True

        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)

        # If there are more than two differing characters, return False
        if len(diff_indices) != 2:
            return False

        # Check if swapping characters at the differing indices makes the strings equal
        return s1[diff_indices[0]] == s2[diff_indices[1]] and s1[diff_indices[1]] == s2[diff_indices[0]]
