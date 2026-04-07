/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        const res = [];
        let queue = [];
        if (root){
            queue.push(root);
        }
        while (queue.length){
            let tempArr = [];

            let length = queue.length;
            for (let i = 0; i < length; i++){
                let curr = queue.shift();
                if(root!==null){
                    tempArr.push(curr.val);  
                }
                if (curr.left){
                    queue.push(curr.left);
                }
                if (curr.right){
                    queue.push(curr.right);
                }
            }
            res.push(tempArr);
        }

        return res;
    }
}
