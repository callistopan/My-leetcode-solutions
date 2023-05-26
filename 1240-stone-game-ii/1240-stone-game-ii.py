class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        # compute the suffix array
        for i in range(n-2,-1,-1):
            piles[i]+=piles[i+1]
            
        
        @lru_cache(None)
        def dp(i,m): # maximum stones the current player can get from piles[i:] with M=m
            if (i+2*m >= n): # last player takes all
                return piles[i]
            
            return piles[i]-min(dp(i+x,max(m,x)) for x in range(1,2*m+1)) 
        return dp(0,1)
        '''
         we have sum of all piles that is suffix -piles[i]
         dp(i+x,max(m,x)) is the piles that can taken by other player ,so we want to minimize the 
         stones taken by other player
         so we check all possible states of stones taken by other player and takes the minimum of 
         it 
         by subtracting from suffix we get our ans
         
         ex : 2 7 9 4 4    //       26 24 17 8  4
         
         i=0 m=1 we have x in range 1-2
         return piles[0]-min(dp(1,1),dp(2,2))
         
         i=1,m=1 dp(1,1) we have x in range 1-2
         return piles[1]-min(dp(2,1),dp(3,2))
         
         each player plays optimally so they all take this condition
         but alice plays first
        '''
        
        
            
        