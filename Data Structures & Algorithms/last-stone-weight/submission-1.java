class Solution {
    public int lastStoneWeight(int[] stones) {
        int res;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for (int stone: stones){
            maxHeap.add(-stone);
        }
        while (maxHeap.size() > 1){
            int temp1 = - maxHeap.poll();
            int temp2 = - maxHeap.poll();
            int tempRes = temp1 - temp2;
            maxHeap.add(- tempRes);
        }
        res = - maxHeap.poll();
        return res;
    }
}
