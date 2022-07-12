#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
	    
	    dp=[i for i in Arr]
	    
	    for i in range(1,n):
	        
	        for j in range(i):
	            
	            if Arr[j] < Arr[i]:
	                
	                dp[i] = max(dp[i],Arr[i]+dp[j])
	                
	    return max(dp)
	                
	                
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends