class Solution:
    '''O(n^3) time
    
    O(n^2) space'''
    def minDistance(self, houses: List[int], k: int) -> int:
        n =len(houses)
        
        # sort the houses
        houses.sort()
        
        # calculate the cost for each sub array when we place the mail box in median position
        costs=[[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                medianPos= houses[(i+j)//2]
                print(medianPos)
                
                for m in range(i,j+1):
                    costs[i][j]+= abs(medianPos-houses[m])
                    
        
                    
                    
        @lru_cache(None)
        
        def dp(k,i):
            
            if k==0 and i==n:
                return 0
            
            if k==0 or i==n:
                return float('inf')
            
            ans =float('inf')
            
            for j in range(i,n):
                cost=costs[i][j]  # put mailbox aty house[i:j]
                
                ans =min(ans,cost+dp(k-1,j+1))
                
            return ans
        
        return dp(k,0)