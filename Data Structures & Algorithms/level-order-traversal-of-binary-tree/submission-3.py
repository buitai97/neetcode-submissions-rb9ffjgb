# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = Queue()
        if root:
            queue.put(root)
        res = []
        while queue.qsize() != 0:
            sublist = []
            for i in range(queue.qsize()):
                cur = queue.get()
                sublist.append(cur.val)
                if cur.left:
                    queue.put(cur.left)
                if cur.right:
                    queue.put(cur.right)
            res.append(sublist)
        
        return res
        
        