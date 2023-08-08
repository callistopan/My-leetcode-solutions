class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        
        l=0
        r=n-1
        
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]<nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid
                    
            else:
                if nums[l]<=target<=nums[mid]:
                    r=mid
                else:
                    l=mid+1
                    
        return -1