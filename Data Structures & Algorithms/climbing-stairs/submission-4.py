class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        def climb(i, cache):
            if i >= n:
                return n == i
            if i in cache:
                return cache[i]
            return climb(i + 1, cache) + climb(i+2, cache)
        return climb(i, {})