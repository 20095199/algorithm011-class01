from typing import List


class Solution:
    def inorder_traversal(self, root)->List[int]:
        """递归"""
        traversal = []
        self.helper(root, traversal)
        return traversal

    def helper(self, root, traversal):
        if not root:
            return
        self.helper(root.left, traversal)
        traversal.append(root.val)
        self.helper(root.right, traversal)

    def inorder_traversal2(self, root)->List[int]:
        stack = []
        traversal = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            traversal.append(cur.val)
            cur = cur.right
        return traversal









