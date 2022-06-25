class Solution:
    '''Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a permutation.'''
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.permute_recursive(nums,0,result)
        return result
    def permute_recursive(self,nums,begin,result):
        
        if begin == len(nums):
            result.append(nums[:])
            return
        
        for i in range(begin,len(nums)):
            nums[begin],nums[i]=nums[i],nums[begin]
            self.permute_recursive(nums,begin+1,result)
            nums[begin],nums[i]=nums[i],nums[begin]
            
        
        
      