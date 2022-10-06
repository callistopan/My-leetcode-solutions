class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        # alice start first
        n=len(piles)
        # compute the suffix array
        for i in range(n-2,-1,-1):
            piles[i]+=piles[i+1]
            
        d={}
        def dp(i): # maximum stones the current player can get from piles[i:] with M=m         
            if (i>=n): return 0
            if i in d:
                return d[i]
            
            d[i]= piles[i]-min(dp(i+x) for x in range(1,4)) 
            return d[i]
        alice=dp(0)
        bob=piles[0]-alice
        if (alice==bob):return "Tie"
        if (alice>bob): return "Alice"
        if (alice<bob):return "Bob"