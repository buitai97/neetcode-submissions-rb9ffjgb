# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = Queue()
        if root:
            q.put(root)
        
        res = []
        while q.qsize() != 0:
            
            for i in range(q.qsize()):
                cur = q.get()
                if i == 0:
                    res.append(cur.val) 
                if cur.right:
                    q.put(cur.right)
                if cur.left:
                    q.put(cur.left)




        return res