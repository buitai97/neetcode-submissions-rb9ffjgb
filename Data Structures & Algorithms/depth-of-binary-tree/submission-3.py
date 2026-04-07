# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root, 0)
    def bfs(self, root, cur_max):
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        return max(self.bfs(root.left, cur_max), self.bfs(root.right, cur_max)) + 1

