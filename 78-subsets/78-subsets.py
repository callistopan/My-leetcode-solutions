class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res =[]
        
        self.backtrack(nums,0,[],res)
        
        return res
    
    
    def backtrack(self,nums,start,subset,res): 
        
        res.append(list(subset))
        
        
        for i in range(start,len(nums)):
            
            
            subset.append(nums[i])
            
            self.backtrack(nums,i+1,subset,res)
            
            subset.pop()
            
     
            
                