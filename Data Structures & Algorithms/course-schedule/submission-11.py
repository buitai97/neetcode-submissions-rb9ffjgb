class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for pre in prerequisites:
            print(pre)
            adj[pre[0]].append(pre[1])

        path = set()

        def dfs(src):
            if src in path:
                return False
            
            if adj[src] == []:
                return True

            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            path.remove(src)
            adj[src] = []
            return True    
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
            
