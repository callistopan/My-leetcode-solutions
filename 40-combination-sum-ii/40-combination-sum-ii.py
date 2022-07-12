class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.dfs(candidates,target,[],res)
        return res
    
    def dfs(self,candidates,target,path,res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        
        for i in range(len(candidates)):
            
            if i>0 and candidates[i]== candidates[i-1]:
                continue
            self.dfs(candidates[i+1:],target-candidates[i],path+[candidates[i]],res)