
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        pre = p
        while head and head.next:
            first, second = head, head.next
            pre.next, first.next, second.next = second, second.next, first
            pre, head = first, first.next
        return p.next


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
