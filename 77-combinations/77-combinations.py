class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        
        results =[]
        candidates =[i for i in range(1,n+1)]
        
        self.backtrack(candidates,comb,k,0,results)
        
        return results
    
    
    def backtrack(self,candidates,comb,k,curr,results):
      
        if k==0:
            
            results.append(list(comb))
            return 
            
        for next_curr in range(curr,len(candidates)):
                
            pick = candidates[next_curr]
            
            comb.append(pick)
            
            self.backtrack(candidates,comb,k-1,next_curr+1,results)
            
            comb.pop()  # back tracking