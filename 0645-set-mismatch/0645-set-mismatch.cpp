class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        // originally contain 1..n
        // so we can negative the position of numbers and if we found the position is already negative then that is the repeating number 
        // we once again traverse the array and a positon is positive then thtat number is missing
        vector<int>res;
        int n=nums.size();
        for (int i=0;i<n;i++){
            if (nums[abs(nums[i])-1]>0){
                nums[abs(nums[i])-1]*=(-1);
            }
            else{
                res.push_back(abs(nums[i]));
            }
        }
        for (int i=0;i<n;i++){
            if (nums[i]>0){
                res.push_back(i+1);
            }
        }
        return res;
    }
};