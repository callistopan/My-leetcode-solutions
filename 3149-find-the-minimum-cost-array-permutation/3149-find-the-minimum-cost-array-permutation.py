class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        self.n = len(nums)
        self.minScore = float("inf")
        self.bestPerm = []
        self.Backtrack(nums,[],[False]*self.n,0)
        return self.bestPerm
    
    def Backtrack(self,nums,currentPerm, used , currentScore):
        
        if len(currentPerm) == self.n:
            # complete the permutation , compare the best found
            # Need to add wrap-around score component
            wrapScore = abs(currentPerm[-1] - nums[currentPerm[0]])
            totalScore = currentScore + wrapScore
            if totalScore < self.minScore:
                self.minScore = totalScore
                self.bestPerm = currentPerm[:]
            return 
        
        for i in range(self.n):
            
            if not used[i]:
                # only proceed if adding this number doesnt exceed the minimum score found yet
                
                if len(currentPerm) > 0:
                    newScore = currentScore + abs(currentPerm[-1] - nums[i])
                    if newScore >= self.minScore:
                        continue
                else:
                    newScore = 0 # start of permutation , no score yet
                used[i] = True
                self.Backtrack(nums,currentPerm +[i], used, newScore)
                used[i] = False
        
        
        