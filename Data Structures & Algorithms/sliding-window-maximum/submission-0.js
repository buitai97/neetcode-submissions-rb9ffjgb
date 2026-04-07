class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        const res = []
        const curWindow = []

        for (let i = 0; i < nums.length; i++){
            curWindow.push(nums[i])
            if(curWindow.length == k){
                res.push(Math.max(...curWindow))
                curWindow.shift()
            }
        }
        return res
    }
}
