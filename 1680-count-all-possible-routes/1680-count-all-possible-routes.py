class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        
        memo={}
        
        
        return self.dfs(locations,start,finish,memo,fuel)
    
    
    '''dp[current_city][fuel] = number of ways to reach finish when at a city with fuel'''
    def dfs(self,locations,curr_city,end ,memo, fuel):
        
        if fuel <0:
            return 0
        
        if (curr_city,fuel) in memo:
            return memo[(curr_city,fuel)]
        
        # atleast one way to reach the city # but don't stop keep going
        
        ans = 1 if curr_city==end else 0
        
        # visit all other cities except self
        
        for nextCity in range(len(locations)):
            
            if nextCity!=curr_city:
                
                ans=(ans+self.dfs(locations,nextCity,end,memo,fuel-abs(locations[curr_city]-locations[nextCity])))%(10**9+7)
                
        memo[(curr_city,fuel)]=ans
        
        return ans
                
                
                