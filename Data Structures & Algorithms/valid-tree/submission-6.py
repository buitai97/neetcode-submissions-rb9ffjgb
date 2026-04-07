class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)]
        for src, des in edges:
            adj[src].append(des)
            adj[des].append(src)
        visited = set()
        q = deque()
        q.append((0, -1))
        visited.add(0)
        while q:
            cur, parent = q.popleft()
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, cur))
            
                visited.add(nei)
        return len(visited) == n

        