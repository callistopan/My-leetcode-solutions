class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        
        while k:
            k -= 1
            m = inf 
            j = 0
            for i in range(n):
                if nums[i] < m:
                    m = nums[i]
                    j = i
            nums[j] *= multiplier
        return nums
        