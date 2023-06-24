class Solution {
public:
    vector<long long> findPrefixScore(vector<int>& nums) {
        vector<long long> res;
        int n = nums.size();
        int  current_max = nums[0];
        long long cover = 0;

        for (int i = 0; i < n; i++){
            current_max = std::max(current_max, nums[i]);
            cover += (current_max + nums[i]);
            res.push_back(cover);
        }
        return res;


    }
};