class Solution:
    def minimumDeletions(self, s: str) -> int:
        l=len(s)
        dp=[0]*(l+1)
        
        b_count=0
        
        for i in range(l):
            if s[i]=='a':
                # either remove current a which is dp[i]+1 cost
                # or remove b's in previous that is b_count
                dp[i+1]=min(dp[i]+1,b_count)
                
            else:
                # valid so no need to remove ,same ans as before
                # increase the b_count
                dp[i+1]=dp[i]
                b_count+=1
                
        return dp[l]
                
        
        
        
        
        
        
        
        
        
        
        
        
        
