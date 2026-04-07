class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        for (int i = 0; i < nums.length; i++){
            int currentSum = nums[i];
            if(i == nums.length - 1){
                maxSum = Math.max(currentSum, maxSum);
                break;
            }
            for (int j = i+1; j < nums.length; j++){
                currentSum = currentSum + nums[j];
                maxSum = Math.max(maxSum, currentSum);
            }
        }
        return maxSum;
    }
}
