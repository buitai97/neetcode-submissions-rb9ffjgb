class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        const res = []
        const queue = []
        let l = 0, r = 0
        while (r < nums.length){
            while (queue != [] && nums[queue[queue.length-1]] < nums[r]){
                queue.pop()
            }
            queue.push(r)
            if (l > queue[0]){
                queue.shift()
            }

            if ((r + 1) >= k){
                res.push(nums[queue[0]])
                l += 1
            } 
            r += 1

            
        }

        return res
    }
}
