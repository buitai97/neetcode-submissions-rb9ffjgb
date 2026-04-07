class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        let res = [];
        let subset = [];
        this.dfs(nums, 0, res, subset);
        return res;
    }
    dfs(nums, i, res, subset){
            if (i >= nums.length){
                res.push([...subset]);
                return;
            }
            subset.push(nums[i]);
            this.dfs(nums, i + 1, res, subset);
            subset.pop();
            this.dfs(nums, i + 1, res, subset);
     }
}
