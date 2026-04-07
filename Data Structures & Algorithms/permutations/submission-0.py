class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(perm, visited):
            if len(perm) == len(nums):
                self.res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    perm.append(nums[i])
                    visited.add(nums[i])
                    dfs(perm, visited)
                    perm.pop()
                    visited.remove(nums[i])
        dfs([], set())

        return self.res
