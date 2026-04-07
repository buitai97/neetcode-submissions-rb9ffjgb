class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1001
        curSum = -1001

        for i in range(len(nums)):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            maxSum = max(curSum, maxSum)

        return maxSum