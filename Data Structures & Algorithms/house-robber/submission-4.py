class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        n = len(nums)
        for i in range(n):
            print(dp)
            if i < 2:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = nums[i] + nums[0]
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp[n - 1], dp[n - 2])
