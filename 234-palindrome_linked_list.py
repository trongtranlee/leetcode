# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head:ListNode)-> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        # Step 1: Traverse the linked list and store elements in a list
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # Step 2: Initialize pointers
        left, right = 0, len(vals) - 1

        # Step 3, 4: Compare elements
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1

        return True
