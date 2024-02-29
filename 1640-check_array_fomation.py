from typing import List


class Solution(object):
    def canFormArray(self, arr:List[int], pieces:List[List[int]])-> bool:
        """
        Input: arr = [91,4,64,78], pieces = [[78],
                                            [4,64],
                                            [91]]
        sortArr = [4,64,78,91]
        Output: true
        Explanation: Concatenate [91] then [4,64] then [78]
        """
        piece_dict = {piece[0]: piece for piece in pieces}
        index = 0

        while index < len(arr):
            if arr[index] in piece_dict:
                piece = piece_dict[arr[index]]
                if arr[index:index + len(piece)] == piece:
                    # Move index to the end of the piece
                    index += len(piece)
                else:
                    # If the rest of the piece doesn't match arr, return False
                    return False
            else:
                # If arr[index] is not found in piece_dict, return False
                return False

        # If all elements in arr are found and matched successfully, return True
        return True



