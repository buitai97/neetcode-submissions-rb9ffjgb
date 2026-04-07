class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        memo[len(nums) - 1] = 0
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            res = 10000000
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        return dfs(0)