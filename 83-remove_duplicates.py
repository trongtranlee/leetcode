# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head:ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:

            #Nếu hai nút kế tiếp có cùng giá trị, chúng ta bỏ qua nút thứ hai.
            if current.next.val == current.next.next.val:
                current.next = current.next.next

            #Nếu không, chúng ta di chuyển tiếp theo trong danh sách.
            else:
                current = current.next

        return dummy.next