class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''   
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        
        '''
        ''' t=O(n) s=O(1) '''
        k=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k+1]=nums[i]
                k+=1
        return k+1