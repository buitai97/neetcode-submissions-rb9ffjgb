class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        prefix = {0:1}
        count = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            diff = sum_ - k
            if diff in prefix:
                count += prefix[diff]
            prefix[sum_] = prefix.get(sum_, 0) + 1
        return count            
            