class Solution:
    
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        '''
        first we need to generate all the possible squares that are less than n
        we can use the squares any number of times for our solution
        we need to find least number of perfect squares
        
        
        ex:
        
             n=12
             
             squares=[1,4,9]
             n=0 0 way
             n=1 1
             
             n=2 1,1
             
             n=3 1,1,1
             
             n=4 1,1,1,1 and 4
             
             n=5 1,1,1,1,1 and 1,4
             
             n=6 1,1,1,1,1,1 and 1,1,4
            
        '''
        if n==1:
            return 1
        dp=[float("inf")]*(n+1)
        
        dp[0]=0
        
        squares =[i**2 for i in range(1,n) if i**2<=n]
        
        
        for square in squares:
            
            for j in range(square,n+1):
                
                dp[j]= min(dp[j],dp[j-square]+1)
                
        return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        