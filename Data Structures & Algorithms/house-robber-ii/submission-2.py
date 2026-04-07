class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[:len(nums) - 1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        rob1, rob2 = 0,0
        for i in range(len(nums)):
            temp = rob2
            rob2 = max(rob1 + nums[i], rob2)
            rob1 = temp
        return rob2