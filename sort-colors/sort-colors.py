class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zero=0
        two=n-1
        
        i=0
        while i<=two:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1
                i+=1
                
            else:
                nums[two],nums[i]=nums[i],nums[two]
                two-=1