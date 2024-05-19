class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # Initialize dp array with -inf (indicating impossible sums)
        dp = [-float('inf')] * (target + 1)
        dp[0] = 0  # Base case: zero sum is achieved with zero elements
        
        for num in nums:
            # Traverse the dp array backwards to prevent using the same element multiple times
            for t in range(target, num - 1, -1):
                if dp[t - num] != -float('inf'):
                    dp[t] = max(dp[t], dp[t - num] + 1)
        
        return dp[target] if dp[target] != -float('inf') else -1