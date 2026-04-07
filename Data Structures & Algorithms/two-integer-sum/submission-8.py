class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
           
            if complement in numMap and i != numMap[complement]:
                return [i, numMap[complement]]