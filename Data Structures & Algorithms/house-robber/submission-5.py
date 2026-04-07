class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        n = len(nums)
        for i in range(n):
            dp[i] = nums[i] if i < 2 else (nums[i] + nums[0]) if i == 2 else (max(dp[i-3], dp[i-2]) + nums[i])
            print(dp)
        #     if i < 2:
        #         dp[i] = nums[i]
        #     elif i == 2:
        #         dp[i] = nums[i] + nums[0]
        #     else:
        #         dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp[n - 1], dp[n - 2])
