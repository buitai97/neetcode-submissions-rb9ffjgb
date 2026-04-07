class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1001
        curSum = 0

        for num in nums:
            curSum = max(num, num + curSum)
            maxSum = max(curSum, maxSum)

        return maxSum