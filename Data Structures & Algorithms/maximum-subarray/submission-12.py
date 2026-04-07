class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1001
        curSum = -1001

        for num in nums:
            curSum = max(num, num + curSum)
            maxSum = max(curSum, maxSum)

        return maxSum