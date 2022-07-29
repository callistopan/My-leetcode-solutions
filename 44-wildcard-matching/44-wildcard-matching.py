class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ''' if pattern is a character and string char is same then check restif 
            if pattern is * then we may skip so many characters or this is just empty 
            when we checked all the chars in string and and all of from p then return true
            ie when s and p becomes empty same time
            if s is empty and if there are other non * chars is pattern then return False
            if pattern is empty return false ,as there is no matching
            if pattern is ? and there is s then we can check  rest else return false
            
        '''
        return self.match(s,p,0,0)
    
    @lru_cache(None)
    def match(self,s,p,i,j):
        
        if j==len(p):
            return i==len(s)
        if p[j]=='*':
            
            return  (i< len(s) and self.match(s,p,i+1,j)) or self.match(s,p,i,j+1)
        
        
        if i <len(s) and (p[j]=='?' or s[i]==p[j]):
            return self.match(s,p,i+1,j+1)
        
        return False
        

        
        
        
        
        
        
        
        
        
        
        
        
        

        
            
        
        