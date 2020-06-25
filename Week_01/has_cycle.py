
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i, j = head, head
        while j and j.next:
            i, j = i.next, j.next.next
            if i == j:
                return True
        return False
            
