class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []
        def dfs(i, total):
            if total == target:
                res.append(curSet.copy())
                return 
            if i >= len(nums) or total > target:
                return
            
            curSet.append(nums[i])
            dfs(i, total + nums[i])

            curSet.pop()

            dfs(i + 1, total)

        dfs(0, 0)
        return res