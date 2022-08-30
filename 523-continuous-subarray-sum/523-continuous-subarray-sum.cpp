class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        
        map<int,int> d={{0,-1}};
        int sum=0;
        
        for(int i=0;i<nums.size();i++){
            
            if (k){
                sum=(sum+nums[i])%k;
            }
            else{
                sum+=nums[i];
            }
            
            if (d.find(sum)==d.end()){
                d[sum]=i; // store the index of the current sum
            }
            else if ((i-d[sum])>=2){
                    return true;
                }
            }
        return false;
        }
        
    
};