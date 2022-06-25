class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.dfs(n,0,0,'',res)
        
        return res
    
    def dfs(self,n,l,r,path,res):
        if len(path)==2*n:
            res.append(path)
            return
            
        if l<n:
            self.dfs(n,l+1,r,path+"(",res)
            
        if r<l:
            self.dfs(n,l,r+1,path+")",res)
            
    