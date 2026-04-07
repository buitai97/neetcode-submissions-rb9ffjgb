class MinStack {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> minStack = new Stack<>();
    public MinStack() {

    }
    
    public void push(int val) {
        stack.add(val);
        if(!minStack.isEmpty()){
            val = Math.min(val, minStack.get(minStack.size() - 1));
        }
        minStack.push(val);

    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        return minStack.get(minStack.size() - 1);
    }
}
