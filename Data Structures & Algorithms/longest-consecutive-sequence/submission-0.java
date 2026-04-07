class Solution {
    public int longestConsecutive(int[] nums) {
        int maxLength = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++ ){
            set.add(nums[i]);
        }

        for (int i = 0; i< nums.length; i++){
            if (set.contains(nums[i]- 1)){
                
                continue;
            }
            else{
                int length = 0;
                while (set.contains(nums[i] + length)){
                    length += 1;
                } 
                maxLength = Math.max(maxLength, length);
            }
        }
        return maxLength;
    }
}
