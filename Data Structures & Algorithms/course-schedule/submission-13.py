class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegrees[dst] += 1
            adj[src].append(dst) 
        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        finished = 0
        while q:
            cur = q.popleft()
            finished += 1
            
            for nei in adj[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
            
        return finished == numCourses
