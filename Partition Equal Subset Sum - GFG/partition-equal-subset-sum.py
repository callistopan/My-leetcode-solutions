# User function Template for Python3

class Solution:
    def equalPartition(self, N, nums):
        # code here
        
        sum_ = sum(nums)
        
        if sum_&1:
            return False
            
        required_sum = sum_//2
        
        # check if we can form this sum using the elements of the array
        
        dp=[False]*(required_sum+1)
        dp[0] = True
        
        
        for num in nums:
            
            if dp[-1]:
                return True
            
            for j in range(required_sum,num-1,-1):
                
                dp[j] = dp[j] or dp[j-num]
                
        return dp[-1]== True
                
            
            
            
        

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends