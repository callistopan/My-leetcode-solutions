from typing import List
from collections import deque

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        res = []
        bad = 0
        for i in range(n):
            if i:
                bad += nums[i] != nums[i-1] + 1
            if i >= k:
                bad -= nums[i- k + 1] != nums[i-k] + 1
            if i >= k - 1:
                res.append(nums[i] if bad == 0 else - 1)
        return res
