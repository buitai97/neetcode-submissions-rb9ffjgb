class TreeNode{
    int key, val;
    TreeNode left;
    TreeNode right;
    TreeNode(int key, int val){
        this.key = key;
        this.val = val;
    }
}
class TreeMap {

    private TreeNode root;
    public TreeMap() {
        root = null;
    }

    public void insert(int key, int val) {
        TreeNode newNode = new TreeNode(key, val);
        if (root == null){
            this.root = newNode;
            return;
        }
        TreeNode cur = root;
        while (cur != null){
            if (key < cur.key){
                if (cur.left == null){
                    cur.left = newNode;
                    return;
                }
                cur = cur.left;
            }
            else if (key > cur.key){
                if (cur.right == null){
                    cur.right = newNode;
                    return;
                }
                cur = cur.right;
            }
            else{
                cur.val = val;
                return;
            }
        }
    }

 private TreeNode findMin(TreeNode node) {
        while (node != null && node.left != null) {
            node = node.left;
        }
        return node;
    }
    public int get(int key) {
        TreeNode cur = root;
        while (cur != null){
            if(key < cur.key){
                cur = cur.left;
            }
            else if(key > cur.key){
                cur = cur.right;
            }
            else{
                return cur.val;
            }
        }
        return -1;
    }

    public int getMin() {
        TreeNode cur = root;
        if (cur == null){
            return -1;
        }
        while (cur.left != null){
            cur = cur.left;
        }
        return cur.val;
    }

    public int getMax() {
        TreeNode cur = root;
        if (cur == null){
            return -1;
        }
        while (cur.right != null){
            cur = cur.right;
        }
        return cur.val;
    }

    public void remove(int key) {
        root = removeHelper(root,key);
    }

    private TreeNode removeHelper(TreeNode curr, int key) {
        if (curr == null) {
            return null;
        }

        if (key > curr.key) {
            curr.right = removeHelper(curr.right, key);
        } else if (key < curr.key) {
            curr.left = removeHelper(curr.left, key);
        } else {
            if (curr.left == null) {
                // Replace curr with right child
                return curr.right;
            } else if (curr.right == null) {
                // Replace curr with left child
                return curr.left;
            } else {
                // Swap curr with inorder successor
                TreeNode minNode = findMin(curr.right);
                curr.key = minNode.key;
                curr.val = minNode.val;
                curr.right = removeHelper(curr.right, minNode.key);
            }
        }
        return curr;
    }

    public List<Integer> getInorderKeys() {
        List<Integer> result = new ArrayList<>();
        inorderTraversal(root, result);
        return result;
    }

    private void inorderTraversal(TreeNode root, List<Integer> result) {
        if (root != null) {
            inorderTraversal(root.left, result);
            result.add(root.key);
            inorderTraversal(root.right, result);
        }
    }
}
