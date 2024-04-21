long long countAlternatingSubarrays(int* nums, int numsSize) {
    long long res = 1, size = 1;
    for (int i = 1; i < numsSize; ++i) {
        size = nums[i - 1] == nums[i] ? 1 : size + 1;
        res += size;
    }
    return res;
}