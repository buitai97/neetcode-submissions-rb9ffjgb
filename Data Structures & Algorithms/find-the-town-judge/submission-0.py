class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for src, dst in trust:
            adj[dst].append(src)
        
        flag = False
        for i in range(len(adj)):
            if len(adj[i]) == n-1:
                flag = True
                for neigh in adj[i]:
                    if i in adj[neigh]:
                        flag = False
                if flag:
                    return i        
        return -1