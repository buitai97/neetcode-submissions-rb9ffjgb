class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int curSum = 0;

        for (int n : nums){
            curSum = Math.max(0, curSum);
            curSum += n;
            maxSum = Math.max(curSum, maxSum);
        }
        return maxSum;
    }
}
