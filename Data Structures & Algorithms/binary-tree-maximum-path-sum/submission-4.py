# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')
        

        def maxPathSubTree(node) -> int:
            if not node:
                return 0
            
            leftPath = max(maxPathSubTree(node.left), 0)
            rightPath = max(maxPathSubTree(node.right), 0)

            current_path = node.val + leftPath + rightPath
            self.maxPath = max(self.maxPath, current_path)


            return max(leftPath, rightPath) + node.val
        maxPathSubTree(root)    
        return self.maxPath