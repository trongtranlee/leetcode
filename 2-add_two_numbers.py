from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize variables
        carry = 0
        dummy = ListNode()  # Dummy node to start the result linked list
        current = dummy  # Pointer to traverse the result linked list

        # Traverse both linked lists
        while l1 or l2 or carry:
            # Calculate the sum of current digits and carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Update carry for next calculation
            carry = total // 10

            # Create a new node with the value being the remainder after dividing by 10
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in the linked lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the next node of the dummy node, which is the start of the result linked list
