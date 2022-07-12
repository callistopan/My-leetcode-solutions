class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        
        results =[]
        self.backtrack(candidates,comb,target,0,results)
        
        return results
    
    def backtrack(self,candidates,comb,target,curr,results):
        
        if target<0:
            return
        if target==0:
            
            results.append(list(comb))
            return 
            
        for next_curr in range(curr,len(candidates)):
            
                
            pick = candidates[next_curr]
            
            comb.append(pick)
            
            self.backtrack(candidates,comb,target-pick,next_curr,results)
            
            comb.pop()