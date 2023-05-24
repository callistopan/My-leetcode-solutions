class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        
        vector<pair<int,int>> engineers;
        for (int i=0;i<n;i++){
            engineers.emplace_back(efficiency[i],speed[i]);
        }
        
        sort(rbegin(engineers),rend(engineers));
        long speedSum=0,ans=0;
        priority_queue<int,vector<int>,greater<int>> minHeap;
        
        for (auto&[e,s]: engineers){
            speedSum+=s;
            minHeap.push(s);
        if (minHeap.size()>k){
            speedSum-=minHeap.top();
            minHeap.pop();
        }
        ans=max(ans,speedSum*e);  // each time we consider lower efficiency than  previi
        }
        
        return ans%(int)(1e9+7);
        
        
    }
};


//(efficeiency ,speed) => [(9,1),(7,5),(5,2),(4,10),(3,3),(2,8)]