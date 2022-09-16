class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int count[201]={};
        int res=0;
        // count each num in the nums
        for(auto n:nums) count[n]++;
        // k apart combinations is just multiple of corresponding count
        for (int i=k+1;i<201;i++)
            res+=count[i]*count[i-k];
        return res;
    }
};