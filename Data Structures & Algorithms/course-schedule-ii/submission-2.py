class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        order.reverse()
        return order if len(order) == numCourses else []