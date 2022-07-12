class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' time complexity is O(2^n) where n=len(combinations)
        
            can be proved using recursion tree'''
        comb = []
        
        results =[]
        candidates.sort()
        
        self.backtrack(candidates,comb,target,0,results)
        
        return results
    
    
    def backtrack(self,candidates,comb,target,curr,results):
        
        if target<0:
            return
        if target==0:
            
            results.append(list(comb))
            return 
            
        for next_curr in range(curr,len(candidates)):
            
            if next_curr > curr and candidates[next_curr]== candidates[next_curr-1]:
                
                continue  # avoid duplicates
                
            pick = candidates[next_curr]
            
            comb.append(pick)
            
            self.backtrack(candidates,comb,target-pick,next_curr+1,results)
            
            comb.pop()  # back tracking
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            