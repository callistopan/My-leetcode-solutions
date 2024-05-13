class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums +[1]
        n = len(nums)
        self.d = {}
        return self.dfs(nums,0,n-1)
    
    def dfs(self,nums,l,r):
        if (l,r) in self.d:
            return self.d[(l,r)]
        
        if l == r:
            return 0
        max_score = 0
        for i in range(l+1, r):
            # burst the current balloon
            score = nums[l] * nums[i] * nums[r] + self.dfs(nums,l,i) + self.dfs(nums,i,r)
            max_score = max(max_score, score)
        self.d[(l,r)]= max_score
        return max_score
            
                