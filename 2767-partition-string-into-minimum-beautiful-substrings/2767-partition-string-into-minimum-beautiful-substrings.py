class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powers_of_five = {bin(5**i)[2:] for i in range(9)}
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            for j in range(i):
                if s[j:i] in powers_of_five:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[n] if dp[n] != float('inf') else -1
        