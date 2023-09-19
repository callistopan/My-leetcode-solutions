class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(n):
            
            if nums[abs(nums[i])]<0:  # previously it was set , so it is a duplicate number
                return abs(nums[i])
            
            nums[abs(nums[i])]*=-1   #set number at this nums[i] index as negative
  