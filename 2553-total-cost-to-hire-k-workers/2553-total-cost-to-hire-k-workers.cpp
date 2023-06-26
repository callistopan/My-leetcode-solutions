class Solution {
public:
    // time complexity O((k+candidates) log(candidates))
    // space O(candidates)  for storing in priority queues
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n  = costs.size();
        priority_queue<int, vector<int>, greater<int>> LeftHeap;
        priority_queue<int, vector<int>, greater<int>> RightHeap;
        // push elements to left heap
        for (int i = 0;i < candidates ; i++){
            LeftHeap.push(costs[i]);
        }
        // push elementws to right heap
        for (int i = n-1; i>= max(candidates,n-candidates);i--){
            RightHeap.push(costs[i]);
        }

        int l = candidates-1;
        int r = max(candidates,n-candidates);
        long long cost = 0;

        while (k--){

            if (!LeftHeap.empty() && !RightHeap.empty()){
                // left heap has the smallest cost
                if (LeftHeap.top() <= RightHeap.top()){
                    cost += LeftHeap.top();
                    LeftHeap.pop();
                    if (l+1<r && l+1<n){
                        l ++;
                        LeftHeap.push(costs[l]);
                    }
                }
                else{
                    cost += RightHeap.top();
                    RightHeap.pop();
                    if (r-1>l && r-1 >=0){
                        r --;
                        RightHeap.push(costs[r]);
                    }
                }
            }
            else if (RightHeap.empty()){
                cost += LeftHeap.top();
                LeftHeap.pop();
            }
            else{
                cost += RightHeap.top();
                RightHeap.pop();
            }

        }
        return cost;
    }
};