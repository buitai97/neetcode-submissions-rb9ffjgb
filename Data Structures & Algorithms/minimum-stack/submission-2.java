class MinStack {
    Stack<Pair<Integer, Integer>> stack = new Stack<>();
    public MinStack() {

    }
    
    public void push(int val) {
        int minVal = val;
        if(!stack.isEmpty()){
            minVal = Math.min(val, stack.peek().getValue());
        }

        Pair<Integer, Integer> pair= new Pair<>(val, minVal);
        stack.push(pair);
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.get(stack.size() - 1).getKey();
    }
    
    public int getMin() {
        return stack.get(stack.size() - 1).getValue();
    }
}
