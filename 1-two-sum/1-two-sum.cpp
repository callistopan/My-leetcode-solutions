class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int,int> d;
        
        vector<int> res;
        for (int i=0;i<nums.size();i++){
            
            if (d.find(target-nums[i])!=d.end()){
                
                res.push_back(i);
                res.push_back(d[target-nums[i]]);
                
                return res;
                
            }
            
            
            d[nums[i]]=i;
        }
        return res;
    }
};