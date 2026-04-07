class KthLargest {
    int k;
    PriorityQueue<Integer> minHeap;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();

        for(int num:nums){
            add(num);
        }
    }
    
    public int add(int val) {
        minHeap.add(val);
        int[] temp = new int[k];
        
        if(minHeap.size() > k){
            minHeap.poll();
        }
        return minHeap.peek();
    }
}
