class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        @cache
        def dfs(l,r):
            if l == r:
                return 0
            max_score = 0
            for i in range(l+1, r):
                # burst the current location
                score = nums[l] * nums[i] * nums[r] + dfs(l,i) + dfs(i,r)
                max_score = max(max_score, score)
            return max_score
        return dfs(0, n - 1)