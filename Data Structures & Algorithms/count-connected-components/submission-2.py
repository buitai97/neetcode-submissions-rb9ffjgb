class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        count = 0 
        for node in range(n):
            if node not in visited:            
                q = deque([node])
                visited.add(node)
                while q:
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                count += 1
        return count