/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        if (root!= null){
            queue.add(root);
        }
        while(!queue.isEmpty()){
            TreeNode cur = new TreeNode(); 
            int levelLength = queue.size();
            for (int i = 0; i< levelLength; i++){
                cur = queue.remove();
                if (cur.left != null ){
                    queue.add(cur.left);
                }
                if (cur.right != null){
                    queue.add(cur.right);
                }
            }
            res.add(cur.val);
        }
        
        return res;
    }
}
