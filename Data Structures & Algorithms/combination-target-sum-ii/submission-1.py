class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_set = []
        candidates.sort()
        visited = set()
        def dfs(index, total):
            if target == total:
                res.append(cur_set.copy())
                return 

            if total > target or index >= len(candidates):
                return            
            
            cur_set.append(candidates[index])
            dfs(index +1 , total + candidates[index])
            cur_set.pop()
            while index < (len(candidates) - 1) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, total)
        dfs(0,0)
        return res