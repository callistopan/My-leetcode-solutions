class Solution {
public:
    
    int maximumScore(int a, int b, int c) {
    if (a < b)
        return maximumScore(b, a, c);
    if (b < c)
        return maximumScore(a, c, b);
    return b == 0 ? 0 : 1 + maximumScore(a - 1, b - 1, c); 
}
    /*int maximumScore(int a, int b, int c) {
        
        priority_queue<int> heap;
        heap.push(a);
        heap.push(b);
        heap.push(c);
        int count=0;
        while (heap.size()){
            auto first_max= heap.top();
            heap.pop();
            auto second_max=heap.top();
            heap.pop();
            
            if (--first_max>0){
                heap.push(first_max);
            }
            if (--second_max>0){
                heap.push(second_max);
            }
            count++;
        }
        return count;
        */
        
    
};