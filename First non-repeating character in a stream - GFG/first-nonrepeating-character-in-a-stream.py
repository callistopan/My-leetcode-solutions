#User function Template for python3
from collections import deque
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
	    q=deque()
	    res=""
		
		chars=[0]*26
		
		for element in A:
		    
		    chars[ord(element)-ord('a')]+=1
		    
		    if ( chars[ord(element)-ord('a')]==1):
		        q.append(element)
		        
		    while q and chars[ord(q[0])-ord('a')]!=1:
		        q.popleft()
		        
		    if q:
		        res+=q[0]
		    else:
		        res+='#'
		        
		 
		        
		return res
		        
		        
		    
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends