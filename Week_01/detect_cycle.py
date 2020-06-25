
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        i, j = head, head
        while j and j.next:
            i, j = i.next, j.next.next
            if i==j:
                while head != i:
                    head, i = head.next, i.next
                return ret
