
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            # head.next, pre, head = pre, head, head.next
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    def reverse_list(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return p
