class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(0, n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([dst,weight])
            adj[dst].append([src,weight])

        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])
        print(adj)
        print("minHeap: ", minHeap)
        mst = []
        visit = set()
        visit.add(0)
        res = 0
        while minHeap:
            weight, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            mst.append([src, node])
            res += weight
            for neighbor, weight in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, node, neighbor])
        
        if len(mst) != n-1:
            return -1
        return res