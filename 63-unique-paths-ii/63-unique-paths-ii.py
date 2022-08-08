class Solution:
    def uniquePathsWithObstacles(self, M: List[List[int]]) -> int:
        if M[0][0]==1:
            return 0
        r=len(M)
        c=len(M[0])
        dp=[[0 for i in range(c)] for j in range(r)]
        dp[0][0]=1
        for j in range(1,c):
              if M[0][j]==0:
                    dp[0][j]=dp[0][j-1]
        for i in range(1,r):
              if M[i][0]==0:
                    dp[i][0]=dp[i-1][0]
        
        for i in range(1,r):
            for j in range(1,c):
                if M[i][j]==0:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
                
        return dp[-1][-1]