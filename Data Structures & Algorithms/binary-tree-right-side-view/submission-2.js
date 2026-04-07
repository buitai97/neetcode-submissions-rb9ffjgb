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
     * @return {number[]}
     */
    rightSideView(root) {
        const res = [];
        const queue = [];
        if (root){
            queue.push(root);
        }
        while (queue.length){
            
            let length = queue.length;
            res.push(queue[0].val);
            for (let i = 0; i < length; i++){
                let curr = queue.shift();
                if (curr.right){
                    queue.push(curr.right);
                }
                if (curr.left){
                    queue.push(curr.left);
                }
            }
        }

        return res;
    }
}
