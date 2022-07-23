class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        
        dp =[[-1 for i in range(fuel+1)] for j in range(n)]
        
        
        return self.dfs(locations,start,finish,dp,fuel)
    
    
    '''dp[current_city][fuel] = number of ways to reach finish when at a city with fuel'''
    def dfs(self,locations,curr_city,end ,dp, fuel):
        
        if fuel <0:
            return 0
        
        if dp[curr_city][fuel]!=-1:
            return dp[curr_city][fuel]
        
        # atleast one way to reach the city # but don't stop keep going
        
        ans = 1 if curr_city==end else 0
        
        # visit all other cities except self
        
        for nextCity in range(len(locations)):
            
            if nextCity!=curr_city:
                
                ans=(ans+self.dfs(locations,nextCity,end,dp,fuel-abs(locations[curr_city]-locations[nextCity])))%(10**9+7)
                
        dp[curr_city][fuel]=ans
        
        return ans
                
                
                