public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        PriorityQueue<int,int> heap = new PriorityQueue<int,int>();
        foreach (int num in nums){
            heap.Enqueue(num,-num);
        }
        int res = 0;
        for (int i = 0; i < k; i ++){
            res = heap.Dequeue();
        }
        
        return res;
    }
}