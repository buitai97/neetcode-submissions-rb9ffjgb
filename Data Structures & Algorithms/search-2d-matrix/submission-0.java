class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int innerLength = matrix[0].length;
        int outerLength = matrix.length;
        int left = 0;
        int right = outerLength * innerLength - 1;

        while (left <= right){
            int mid = (left + right) / 2;
            int rowMid = mid / innerLength;
            int colMid = mid % innerLength;

            if (target < matrix[rowMid][colMid]){
                right = mid - 1;
            }
            else if(target > matrix[rowMid][colMid]){
                left = mid + 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
}
