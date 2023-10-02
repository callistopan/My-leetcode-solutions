class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    int i = 0;
    for (int num : nums)
        if (i < 2 || num > nums[i-2]) // check previous previous num is less than this one to make sure no more than 2 numbers is allowed
            nums[i++] = num;
    return i;
}
};