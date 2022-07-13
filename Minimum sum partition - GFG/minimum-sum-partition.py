#User function Template for python3
from functools import lru_cache 
import sys
class Solution:
	def minDifference(self, a, n):
	    su = 0
 
        # Calculate sum of all elements
        su = sum(a)
     
        # Create an 2d list to store
        # results of subproblems
        dp = [[0 for i in range(su + 1)]
              for j in range(n + 1)]
    
        for i in range(n + 1):
            dp[i][0] = True
     
        for j in range(1, su + 1):
            dp[0][j] = False
     
        for i in range(1, n + 1):
            for j in range(1, su + 1):
     
                # If i'th element is excluded
                dp[i][j] = dp[i - 1][j]
     
                # If i'th element is included
                if a[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - a[i - 1]]
     
        diff = sys.maxsize
     
        
        for j in range(su // 2, -1, -1):
            if dp[n][j] == True:
                diff = su - (2 * j)
                break
     
        return diff
    	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
		# code here
		sum_ =sum(arr)
		
		return self.dfs(tuple(arr),n,0,sum_)
		
	@lru_cache(200)
	def dfs(self,arr,i,curr_sum,sum_):
	    
	    # if we have reached the last element sum of one set is curr_sum and other set we cand find
        
        
        if i==0:
            
            return abs(  curr_sum - (sum_ - curr_sum) )
            
        # we have two choices either include  the arr[i-1] or not include
        
        return min(self.dfs(arr,i-1,curr_sum+arr[i-1],sum_) , self.dfs(arr,i-1,curr_sum,sum_))
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends