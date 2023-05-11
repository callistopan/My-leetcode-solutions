class Solution:
    def maxUncrossedLines(self, num1: List[int], num2: List[int]) -> int:
        n=len(num1)
        m=len(num2)
        dp=[[0 for i in range(n+1) ] for j in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if num2[i-1]==num1[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        