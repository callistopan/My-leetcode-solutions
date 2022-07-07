class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ''' ababaabbacd'''
        res=[]
        
        self.dfs(s,[],res)
        
        return res
    
 
    def dfs(self,s,path,res):
        
        if len(s)==0:
            res.append(path)
            
            return
        t=''
        for  i in range (len(s)):
            
            t+=s[i]
            
            if self.check(t):
                self.dfs(s[i+1:],path+[t],res)
                
            
        
    def check(self,s):
        
        l=0
        r=len(s)-1
        
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
            
        return True
        