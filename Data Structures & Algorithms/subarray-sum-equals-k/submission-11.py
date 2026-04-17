class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        prefix = {0:1}
        count = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            diff = sum_ - k
            count += prefix.get(diff, 0)
            prefix[sum_] = prefix.get(sum_, 0) + 1
        return count            
            