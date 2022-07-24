class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ele=float('-inf')
        
        for i in range(len(nums)):
            
            if nums[i] >max_ele:
                max_ele=nums[i]
                index=i
        
        print(max_ele)
        for num in nums:
            if num!=max_ele and max_ele <2*num:
                return -1
            
        return index