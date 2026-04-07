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
        while (l1 || l2 || carried) {
            const val1 = l1?l1.val:0
            const val2 = l2?l2.val:0
            
            let curSum = val1 + val2 + carried
            carried = Math.floor(curSum/10)
            curSum = curSum % 10
            curr.next = new ListNode(curSum)
            curr = curr.next

            l1 = l1?l1.next : null
            l2 = l2?l2.next : null
            
        }

        return resultHead.next
    }
}
