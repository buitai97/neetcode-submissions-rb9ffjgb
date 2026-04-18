# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            res = 0
            if root.val in range(low, high + 1):
                res += root.val
            res += dfs(root.left)
            res += dfs(root.right)
            return res
        return dfs(root)