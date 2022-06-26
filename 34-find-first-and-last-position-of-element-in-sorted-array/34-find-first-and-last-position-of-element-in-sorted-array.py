class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ''' search for position of target-1 and target+1 '''
        if not self.binarySearchc(nums,target):
            return [-1,-1]
        left_index=self.binarySearch(nums,target-1)
        right_index=self.binarySearch(nums,target)
        return [left_index,right_index-1]
        
        
        
        
    
    def binarySearch(self,nums,target):
        l=0
        r=len(nums)
        
        while l < r:
            mid= l+(r-l)//2
            if nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return l
    
    def binarySearchc(self,nums,target):
        l=0
        r=len(nums)
        
        while l < r:
            mid= l+(r-l)//2
            if nums[mid]==target:
                return True
            if nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return False