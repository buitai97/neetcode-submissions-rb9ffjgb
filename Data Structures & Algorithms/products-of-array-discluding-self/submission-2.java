class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int prefix[] = new int[n];
        int postfix[] = new int[n];
        int prefixProduct = 1;
        for (int i = 0; i < n; i++){
            prefixProduct *= nums[i];
            prefix[i] = prefixProduct;
        }
        int postfixProduct = 1;
        for (int i = nums.length - 1; i >= 0; i--){
            postfixProduct *= nums[i];
            postfix[i] = postfixProduct;
        }

        int[] output = new int[n];

        for (int i = 0; i < n; i++){
            if (i == 0){
                output[i] = postfix[i + 1];
            }
            else if (i == n - 1){
                output[i] = prefix[i - 1];
            }
            else{
                int left = prefix[i - 1];
                int right = postfix[i + 1];
                output[i] = left * right;
            }
        }
        return output;
    }
}  
