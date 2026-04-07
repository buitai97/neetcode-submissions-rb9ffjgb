class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curMin = 0
        minSum = nums[0]

        curMax = 0
        maxSum = nums[0]
        for n in nums:
            curMin = min(n, curMin + n)
            minSum = min(minSum, curMin)

            curMax = max(n, curMax + n)
            maxSum = max(curMax, maxSum)
        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)