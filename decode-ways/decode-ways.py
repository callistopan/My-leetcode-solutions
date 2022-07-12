class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        ex "12" 2
        "123"  1 2 3  ,12 3 ,1 23  -3
        
        '''
        n= len(s)
        
        dp =[0]*(len(s)+1)
        
        dp[0]=1
        
        dp[1]= 0 if s[0]=='0' else 1
        
        for i in range(2,n+1):
            
            onedigit = s[i-1]
            twodigit = s[i-2:i]
            
            if int(onedigit) >=1:
                
                dp[i]+=dp[i-1]
                
            if int(twodigit) >=10 and int(twodigit)<=26:
                
                dp[i]+=dp[i-2]
                
        return dp[-1]
    
 
    ''' without lru_cache we have a O(2^len(A)) time complexity'''
    def numDecodings2(self, A: str) -> int:
        
        @lru_cache(None)
        def dfs(i):
            
            if i == len(A):
                
                return 1
            
            ans =0
            
            if A[i]!='0':
                ans+=dfs(i+1)  # single digit
                
            if i+1 <len(A) and (A[i]=='1' or A[i]=='2' and A[i+1]<='6'):  # possible 2 digit
                
                ans+=dfs(i+2)
                
            return ans
        
        return dfs(0)