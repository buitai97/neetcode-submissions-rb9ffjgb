class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for i in range(len(nums))]
        postfix = [0 for i in range(len(nums))]
        res = [0 for i in range(len(nums))]
        curProduct = 1
        for i in range(len(nums)):
            curProduct *= nums[i]
            prefix[i] = curProduct
        curProduct = 1
        for i in range(len(nums)-1, -1,-1):
            curProduct *= nums[i]
            postfix[i] = curProduct
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else: 
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res