class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        map<int,int> d;
        int sum=0;
        int count=0;
        
        for(int i=0;i<nums.size();i++){
            
            sum+=nums[i];
            
            if (sum==k){
                count++;
                
            }
            
             if (d.find(sum-k)!=d.end()){
                count+=d[sum-k];
            }
            
            if (d.find(sum)!=d.end()){
                d[sum]++;
            }
            else{
                d[sum]=1;
            }
            
        }
        
        return count;
        
    }
};