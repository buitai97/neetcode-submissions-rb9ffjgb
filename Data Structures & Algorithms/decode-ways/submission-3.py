class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i : int) -> int:
            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            memo[i] = res
            return res    

        res = dfs(0)
        return res