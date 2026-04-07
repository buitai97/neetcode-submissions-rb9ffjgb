class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i : int) -> int:
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0
            res = 0
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            res += dfs(i + 1)
            memo[i] = res
            return res    

        res = dfs(0)
        return res