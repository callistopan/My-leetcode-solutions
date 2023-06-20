class Solution {
public:
    int dp[262144] = {};
int dfs(vector<int>& nums, int i, int numSlots, int m) {
    if (i >= nums.size()) 
        return 0;
    if (dp[m] == 0)
        for (int s = 0; s < numSlots; ++s)
            if (m & (1 << s) || m & (1 << (s + numSlots)))
                dp[m] = max(dp[m], ((s + 1) & nums[i]) + 
                    dfs(nums, i + 1, numSlots, m - (m & (1 << s) ? 1 << s : 1 << (s + numSlots))));
    return dp[m];
}
int maximumANDSum(vector<int>& nums, int numSlots) {
    return dfs(nums, 0, numSlots, (1 << (2 * numSlots)) - 1);
}
};