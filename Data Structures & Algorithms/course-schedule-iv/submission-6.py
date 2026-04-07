class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)

        def dfs(src, dst, visited):
            if src == dst:
                return True
            visited.add(src)

            for nei in adj[src]:
                if nei not in visited:
                    if dfs(nei, dst, visited):
                        return True
            return False

        ans = []
        for src, dst in queries:
            ans.append(dfs(src, dst, set()))
        
        return ans
