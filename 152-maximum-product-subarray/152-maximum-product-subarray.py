class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
          - initialize the maximum product so far and min product so far with first element
          - iterate over rest of numbers
          1. if the number is positive then its just the kadanes algorithm
              in which we multiply curr max with current number and take the maximum of this or the current element
              
          2. if the number is -ve then multiply this with the current min so far 
             
             
          in both cases we need to  update the current max so far and current min so far
          
          the final answer is updated as result
          
          [2,3,-2,4]
        
        '''
        
        n = len(nums)
        
        curr_max = nums[0]  #2
        
        curr_min = nums[0] #2
        
        result   = nums[0] #2

        
        for i in range(1,n): #3 -2 4
            
            if nums[i] >=0 :
                
                curr_max = max(nums[i], curr_max*nums[i]) #6  #-8
                
                curr_min = min(nums[i],curr_min*nums[i])  #3  #-48
                
            else:
                
                temp =curr_max  #6
                
                curr_max = max(nums[i],curr_min*nums[i]) # -2
                
                curr_min = min(nums[i],temp*nums[i])  #-12
                
            
            result =max(result, curr_max) #6
            
        return result
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        