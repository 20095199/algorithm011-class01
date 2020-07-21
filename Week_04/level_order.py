from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """bfs"""
        if not root: return []
        rst = []
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            tmp = []
            for _ in range(q_len):
                node = q.popleft()
                tmp.append(node.val)
                node.left and q.append(node.left)
                node.right and q.append(node.right)
            rst.append(tmp)
        return rst

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """dfs"""
        if not root: return []
        rst = []

        def dfs(node, level):
            if not node:
                return
            if len(rst) < level:
                rst.append([])
            rst[level-1].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return rst



        
        
