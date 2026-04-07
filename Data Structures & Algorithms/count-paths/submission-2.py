class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        for r in range(m):
            cache[(r, n-1)] = 1
        for c in range(n):
            cache[(m-1, c)] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                print(r, c)
                if (r,c) not in cache:
                    cache[(r,c)] = cache[(r+1,c)] + cache[(r,c+1)]
        return cache[(0,0)]