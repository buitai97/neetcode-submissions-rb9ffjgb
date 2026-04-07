/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        let resultHead = new ListNode()
        let curr = resultHead
        let carried = 0
        while (l1 != null || l2 != null) {
            let val1 = 0
            let val2 = 0
            if (l1 != null ) {
                console.log(l1.val)
                val1 = l1.val
                l1 = l1.next
            }
            if (l2 != null){
                val2 = l2.val
                l2 = l2.next
            }
            let curSum = val1 + val2 + carried
            carried = 0
            if (curSum >= 10) {
                curSum = curSum - 10
                carried = 1
            }
            curr.val = curSum

            if(l1 != null || l2 != null || carried != 0){
                const newNode = new ListNode()
                curr.next = newNode
                curr = curr.next
                
            }
            
        }
        if (carried != 0){
            curr.val = 1
        }
        return resultHead
    }
}
