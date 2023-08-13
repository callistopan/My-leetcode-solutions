class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        
        memo={}
        return self.check(nums,0,memo)
    
    
    def check(self,nums,index,memo):
        
        if index in memo:
            return memo[index]
        if index==len(nums):
            return True
        
        if index+1 <len(nums) and nums[index]==nums[index+1] and self.check(nums,index+2,memo):
            memo[index]=True
            return True
        
        if index+1 <len(nums) and index+2<len(nums) and nums[index]==nums[index+1] and  nums[index+1]== nums[index+2]  and self.check(nums,index+3,memo):
            memo[index]=True
            return True
        
        if index+1 <len(nums) and index+2<len(nums) and nums[index]==nums[index+1]-1 and  nums[index+1]== nums[index+2]-1  and self.check(nums,index+3,memo):
            memo[index]=True
            return True
        memo[index]=False
        return False
        
        