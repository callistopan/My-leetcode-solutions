class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n, m = len(nums), max(nums) + 1
        dp , dp2 = [1] * m, [0] * m
        
        for i in range(1, n):
            d = max(0, nums[i] - nums[i - 1])  # Minimum value for arr1[i] to ensure arr1 is non-decreasing
            for j in range(d, nums[i] + 1):  # Loop through possible values for arr1[i]
                dp2[j] = (dp2[j - 1] + dp[j - d]) % mod  # Calculate cumulative valid counts for arr1[i] = j
            print(dp2)
            dp, dp2 = dp2, [0] * m  # Update dp for the next iteration and reset dp2 for new computation
        
        return sum(dp) % mod  # Return the sum of all valid sequences at the last index
