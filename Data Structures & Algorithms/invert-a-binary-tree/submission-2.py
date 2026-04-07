# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invertSubTree(root)
        return root
    def invertSubTree(self, node):
        if not node:
            return 

        if not node.left and not node.right:
            return node

        temp = node.left
        node.left = node.right
        node.right = temp

        if node.left:
            self.invertTree(node.left)
        if node.right:
            self.invertTree(node.right)
        