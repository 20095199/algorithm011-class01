# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return 
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        root.left = self.build_tree(preorder[1:ind+1], inorder[:ind])
        root.right = self.build_tree(preorder[ind+1:], inorder[ind+1:])
        return root



        

