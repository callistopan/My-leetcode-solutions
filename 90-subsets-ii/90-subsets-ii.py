class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        
        self.backtrack(nums,0,[],res)
        
        return res
    
    
    def backtrack(self,nums,start,subset,res): 
        
        res.append(list(subset))
        
        
        for i in range(start,len(nums)):
            ''' skip duplicates'''
            if i>start and nums[i]==nums[i-1]:
                continue
            
            
            subset.append(nums[i])
            
            self.backtrack(nums,i+1,subset,res)
            
            subset.pop()
            