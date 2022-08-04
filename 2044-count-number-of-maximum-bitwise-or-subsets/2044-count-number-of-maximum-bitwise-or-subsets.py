class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s=self.subsets(nums)
        max_possible_or=0
        
        for i in nums:
            max_possible_or|=i

        count=0
        for sub in s:
            
            if sub:
                orr=0
                for i in sub:
                    orr|=i
                if orr==max_possible_or:
                    count+=1
        return count
        
        
        
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