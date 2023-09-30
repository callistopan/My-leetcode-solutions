class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if (nums.size() <3){
            return false;
        }

        stack<int> stk;
        vector<int> min_array(nums.size());
        min_array[0] = nums[0];

        // find the min array

        for ( size_t i = 1; i< nums.size(); i++){
            min_array[i] = min(min_array[i-1] , nums[i]);
        }

        for( size_t j = nums.size() -1 ; j>0 ;j--){
            if (nums[j] <= min_array[j]){ // 13 is not possible
                continue;
            }

            while ( !stk.empty() and stk.top() <= min_array[j]){ // 1 >= 2 , so it should be popped
                stk.pop();
            }

            if (!stk.empty() and stk.top() < nums[j]){ // jpossible 32 , so 132
                return true;

            }
            stk.push(nums[j]);
        }
    return false;

    }
};