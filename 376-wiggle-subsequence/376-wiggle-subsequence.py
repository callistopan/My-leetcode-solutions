class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
       
        
        
        '''
        if not nums:
            return 0
        
        length = 1
        up = None # current is increasing or not
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length
    
    def wiggledp(self,nums):
        
        n=len(nums)
        
        if n<2:
            return n
        
        up=[0]*n
        
        down=[0]*n
        
        for i in range(1,n):
            for j  in range(i):
                
                if nums[i]>nums[j]:
                    up[i]=max(up[i],down[j]+1)
                
                elif nums[i]<nums[j]:
                    down[i]=max(down[i],up[j]+1)
                    
        return 1+max(down[-1],up[-1])