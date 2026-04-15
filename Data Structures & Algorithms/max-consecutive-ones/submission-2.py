class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        i = 0
        if len(nums) == 1:
            return nums[0] 
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_ = max(max_, count)
            i+=1
        return max_