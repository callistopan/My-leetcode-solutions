class Solution:
    ''' 1 2 5
    
        amount =11
          1 2 3 4 ................  coin 1
          
          1 1 2 2 3 ................. coin 2
          
                  1 2          3       coin 5    
          
        0 1 2 3 4 5 6 7 8 9 10 11'''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)

            
        return dp[amount] if dp[amount]!=float('inf') else -1