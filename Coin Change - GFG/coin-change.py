#User function Template for python3

class Solution:
    def count(self, coins, m, amount): 
        # code here 
        
        dp=[0]*(amount+1)
        dp[0]=1
        
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]+=dp[x-coin]
                

            
        return dp[amount] if dp[amount]!=float('inf') else -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends