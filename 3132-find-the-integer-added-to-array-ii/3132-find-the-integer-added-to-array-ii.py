class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        count1 , count2  = Counter(nums1), Counter(nums2)
        for x in range(-1000, 1000):
            is_valid = True
            for y in nums2:
                if count1[y-x] < count2[y]:
                    is_valid = False
            if is_valid:
                return x
                
            