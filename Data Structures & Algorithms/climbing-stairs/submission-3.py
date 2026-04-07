class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        def dfs(i):
            if i >= n:
                return n == i
            return dfs(i+1) + dfs(i+2)
        return dfs(i)