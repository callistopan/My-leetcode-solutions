// using System;
// using System.Collections.Generic;

public class Solution {
    public long[] UnmarkedSumArray(int[] nums, int[][] queries) {
        long sumVal = 0;
        long[] ans = new long[queries.Length];
        var pq = new SortedSet<Tuple<int, int>>(Comparer<Tuple<int, int>>.Create((x, y) =>
        {
            int compare = x.Item1.CompareTo(y.Item1);
            if (compare == 0)
                return x.Item2.CompareTo(y.Item2); // Compare by index if values are equal
            return compare;
        }));

        for (int i = 0; i < nums.Length; i++) {
            sumVal += nums[i];
            pq.Add(new Tuple<int, int>(nums[i], i));
        }

        for (int qIndex = 0; qIndex < queries.Length; qIndex++) {
            var q = queries[qIndex];
            sumVal -= nums[q[0]];
            nums[q[0]] = 0;

            while (pq.Count > 0 && q[1] > 0) {
                var tuple = pq.Min;
                pq.Remove(tuple);
                int val = tuple.Item1;
                int idx = tuple.Item2;

                if (nums[idx] != 0) {
                    sumVal -= nums[idx];
                    nums[idx] = 0;
                    q[1]--;
                }
            }

            ans[qIndex] = sumVal;
        }

        return ans;
    }
}
