class Solution {
public:
    int findValueOfPartition(vector<int>& nums) {
        
        sort(nums.begin(),nums.end());

        // value should be minimized
        int val = INT_MAX;

        for (int i = 0; i < nums.size()-1; i++){
            val = min(val,abs(nums[i]-nums[i+1]));
        }
        return val;
    }
};