class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        count = 0 
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:            
                dfs(node)
                count += 1
        
        return count