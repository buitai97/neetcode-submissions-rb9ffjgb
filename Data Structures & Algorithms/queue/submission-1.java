public class ListNode {
    int val;
    ListNode next;

    public ListNode(int val){
        this.val = val;
        this.next = null;
    }
}
class Deque{
    ListNode left;
    ListNode right;
    public Deque() {
        this.left = null;
        this.right = null;
    }

    public boolean isEmpty() {
        return left == null;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        if (this.right == null){
            this.right = newNode;
            this.left = newNode;
            return;
        }
        this.right.next = newNode;
        this.right = this.right.next;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
        if (this.right == null){
            this.right = newNode;
            this.left = newNode;
            return;
        }
        newNode.next = this.left;
        this.left = newNode;
    }

    public int pop() {
        if (left == null){
            return -1;
        }
        else if (left.next == null){
            int ans = left.val;
            left = null;
            right = null;
            return ans;
        }
        ListNode temp = left;
        while (temp.next != right){
            temp = temp.next;
        }
        int ans = right.val;
        temp.next = null;
        right = temp;
        return ans;
    }

    public int popleft() {
        if(left == null){
            return -1;
        }
        else if (left.next == null){
            int ans = left.val;
            left = null;
            right = null;
            return ans;
        }
        int ans = left.val;
        left = left.next;

        return ans;
    }
}
