class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = 0
        prev = 0
        i = 0
        while k > 0 and i < len(nums):
            l = nums[i] - prev - 1
            if l > k:
                l = k
            if l > 0:
                end = prev + l
                s += (end * (end +1)//2) - (prev* (prev +1)//2)
                k -= l
            prev = nums[i]
            i+=1
        
        if k > 0:
            end = prev + k
            s += (end * (end +1)//2) - (prev * (prev +1)//2) 
        return s