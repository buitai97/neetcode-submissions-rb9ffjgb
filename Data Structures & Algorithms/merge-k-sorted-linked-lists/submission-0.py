# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for head in lists:
            while head:  
                heapq.heappush(min_heap, head.val)
                head = head.next
        res = ListNode()
        cur = res
        for i in range(len(min_heap)):
            cur.next = ListNode(heapq.heappop(min_heap))
            cur = cur.next
        return res.next