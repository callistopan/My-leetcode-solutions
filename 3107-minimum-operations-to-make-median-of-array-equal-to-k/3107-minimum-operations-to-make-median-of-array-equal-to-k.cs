public class Solution {
    public long MinOperationsToMakeMedianK(int[] nums, int k) {
        long res = 0;
        Array.Sort(nums);
        int numsSize = nums.Length;
        for (int i = 0; i <= numsSize / 2; i++)
        {
            res += Math.Max(0, nums[i] - k); // decrease excess numbers
        }

        for (int i = numsSize / 2; i < numsSize; i++)
        {
            res += Math.Max(0, k - nums[i]);
        }

        return res;
    }
}