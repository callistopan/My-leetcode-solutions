class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        
        if len(nums)==0:
            
            return 0
        nums.sort()
        print(nums)
        m=0
        c=0
        for i in range(len(nums)-1):
            
            if nums[i+1]-nums[i]==1:
                c+=1
                if c>m:
                    m=c
            else:
                
                c=0
            
        return m+1
            
        