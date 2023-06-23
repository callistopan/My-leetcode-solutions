class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp ={}

        for right in range(n):
            for left in range(0,right):
                diff = nums[right]-nums[left]
                dp[(right,diff)] = dp.get((left,diff),1) + 1

        return max(dp.values())
