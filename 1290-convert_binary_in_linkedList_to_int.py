# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head:ListNode)-> int:
        """
        Input: head = [1,0,1]
        Output: 5
        Explanation: (101) in base 2 = (5) in base 10
        """
        current = head
        res = []
        while current:
            res.append(str(current.val))
            current = current.next
        binary_number = '0b' + ''.join(res)
        decimal_number = int(binary_number, 2)
        return decimal_number

