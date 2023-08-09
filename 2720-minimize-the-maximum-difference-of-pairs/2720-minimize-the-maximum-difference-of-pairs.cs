public class Solution {
    public int MinimizeMax(int[] nums, int p) {
        Array.Sort(nums);
        int n = nums.Length;

        int left =0, right = nums[n-1]-nums[0] ;// maximum diff possible


        while (left < right) {
            int mid = left + (right - left) / 2;

            // If there are enough pairs, look for a smaller threshold.
            // Otherwise, look for a larger threshold.
            if (countValidPairs(nums, mid) >= p) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int countValidPairs(int[] nums,int threshold){
        int index = 0;
        int count = 0;

        while (index <nums.Length -1){

            if (nums[index +1] - nums[index] <= threshold){
                count+=1;
                index +=1;

            }

            index +=1;

        }
        return count;
    }
}