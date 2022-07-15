class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        ''' iterate over nums and update the maximum index we can reach each time
            whenever we find a index that is greater than the max index then there is no 
            possible way to reach this point ,so we return false else return true'''
        max_index=0
        
        for i in range(len(nums)):
            if i >max_index:
                return False
            max_index=max(max_index,i+nums[i])
        return True