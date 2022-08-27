class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int res=INT_MIN,rows=matrix.size(),cols=matrix[0].size();
        for(int l=0;l<cols;l++){
            vector<int> sums(rows);
            for(int r=l;r<cols;r++){
                for(int i=0;i<rows;i++){
                    sums[i]+=matrix[i][r];
                }
                
                set<int> s={0};
                int curr_sum=0;
                for(int sum:sums){
                    curr_sum+=sum;
                    auto it =s.lower_bound(curr_sum-k);
                    if (it!=end(s)){
                        res=max(res,curr_sum-*it);
                    }
                    s.insert(curr_sum);
                }
            }
            
            
        }
        return res;
        
    }
};