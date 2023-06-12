class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [x*k for k in range(n)]
        print(res)

        for i in range(n):
            cur = nums[i]

            for k in range(n):
                cur = min(cur,nums[i-k])
                res[k] += cur
                
        print(res)
        return min(res)