class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        
        for i in range(1,n):
            dp[i]=dp[i-1]*nums[i-1]
            
        print(dp)
            
        product=1
        ''' basically product will compute the products in reverse order'''
        
        ''' traverse from backwards '''
        for i in range(n-1,-1,-1):
            dp[i]=dp[i]*product
            product*=nums[i]
            
        return dp