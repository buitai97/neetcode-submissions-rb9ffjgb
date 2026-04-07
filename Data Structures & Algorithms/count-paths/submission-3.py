class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
    
        def bruteForce(r, c):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = bruteForce(r + 1, c) +  bruteForce(r, c + 1)
            return cache[(r,c)]
        return bruteForce(0,0)