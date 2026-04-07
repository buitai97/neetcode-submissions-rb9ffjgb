class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, 0]
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            print(dp)
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp
        return dp[1]
