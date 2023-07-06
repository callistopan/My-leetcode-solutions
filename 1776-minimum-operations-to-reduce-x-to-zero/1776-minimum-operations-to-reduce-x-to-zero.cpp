class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int sum = accumulate( nums.begin(), nums.end(),0);
        int max_len = 0;
        int target = sum - x ;// find sub-array with this target sum
        if (target == 0){
            return nums.size();
        }

        int left = 0 , right = 0 , current_sum = 0;

        for ( right = 0 ; right < nums.size(); right++){
            current_sum += nums[right];

            while (( current_sum > target ) && left <= right){
                current_sum -= nums[left];
                left++;
            }

            if (current_sum == target){
                max_len = max( max_len , right - left +1);
            }


        }
        return max_len ? nums.size() - max_len : -1;


    }
};