class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int>seq;
        dfs(res,seq,nums,0);
        return res;
    }
    
    void dfs(vector<vector<int>>& res,vector<int>& seq,vector<int>& nums,int pos){
        
        if (seq.size()>=2){
            res.push_back(seq);
        }
        unordered_set<int> d;
        
        for (int i=pos;i<nums.size();i++){
            
            if ((seq.empty() or nums[i]>=seq.back()) and d.find(nums[i])==d.end()){
                seq.push_back(nums[i]);
                dfs(res,seq,nums,i+1);
                seq.pop_back();
                d.insert(nums[i]);
            }
        }
    }
};