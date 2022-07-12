class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ''' time complexity is O(2^n) where n=len(combinations)
        
            can be proved using recursion tree'''
        comb = []
        
        target=n
        
        results =[]
    
        candidates = [i for i in range(1,10)]
        
        self.backtrack(candidates,comb,target,0,results,k)
        
        return results
    
    
    def backtrack(self,candidates,comb,target,curr,results,k):
        
        if target<0:
            return
        if k==0 and  target==0:
            
            results.append(list(comb))
            return 
            
        for next_curr in range(curr,len(candidates)):
        
            pick = candidates[next_curr]
            
            comb.append(pick)
            
            self.backtrack(candidates,comb,target-pick,next_curr+1,results,k-1)
            
            comb.pop()  # back tracking