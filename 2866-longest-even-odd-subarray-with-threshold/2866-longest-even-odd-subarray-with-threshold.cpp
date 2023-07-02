class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        int res = 0;
        for (int l =0, count = 0; l <nums.size();++l){
            if (nums[l] <= threshold){
                if (count){ // there is a possible sequence of alternating sequence
                    count = nums[l] % 2 == nums[l-1] % 2 ? 0 : count + 1;
                }
                if (count==0){ // may be start of sequence
                    count = nums[l] %2 == 0;
                }

            }
            else{
                count = 0;
            }
            res = max(res , count);
        }
        return res;
    }
};