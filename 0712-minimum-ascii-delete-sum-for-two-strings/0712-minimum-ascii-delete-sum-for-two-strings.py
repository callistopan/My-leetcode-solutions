class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][0]+ord(s1[i-1])  # no s2 , so  we need to delete entair s1
        for j in range(1,m+1):
            dp[0][j]=dp[0][j-1]+ord(s2[j-1])
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1])) # delete that character
        return dp[-1][-1]
        
        
        
        
        
        
        
    
