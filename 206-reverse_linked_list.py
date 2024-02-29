# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head:ListNode)-> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next  # Store the next node
            current_node.next = prev_node  # Reverse the pointer
            prev_node = current_node  # Move prev_node to the current node
            current_node = next_node  # Move current_node to the next node
        return prev_node


