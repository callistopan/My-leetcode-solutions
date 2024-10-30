from typing import List
from math import inf

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis_length = self.getLongestIncreasingSubsequenceLength(nums)
        lds_length = self.getLongestIncreasingSubsequenceLength(nums[::-1])[::-1]
        
        min_removals = inf
        for i in range(1, n - 1):
            if lis_length[i] > 1 and lds_length[i] > 1:  # proper mountain
                min_removals = min(min_removals, n - (lis_length[i] + lds_length[i] - 1))
        
        return min_removals if min_removals != inf else 0

    def getLongestIncreasingSubsequenceLength(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lis = [1] * n
        sub = []
        
        for i in range(n):
            index = self.findPosition(sub, nums[i])
            if index == len(sub):
                sub.append(nums[i])
            else:
                sub[index] = nums[i]
            lis[i] = len(sub)
        
        return lis

    def findPosition(self, nums: List[int], e: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < e:
                l = m + 1
            else:
                r = m - 1
        
        return l
