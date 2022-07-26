class Solution:
    def numSplits(self, s: str) -> int:
        
        d={}
        n=len(s)
        
        # compute left and right unique chars in the s 
        
        # for 0..i
        
        prefix=[0]*n
        
        for i in range(n):
            
            d[s[i]]=True
            
            prefix[i]=len(d)
            
        # for i+1 ...n
        print(prefix)
        
        d.clear()
        
        suffix=[0]*n
        
        for i in range(n-2,-1,-1):
            
            d[s[i+1]]=True
            
            
            suffix[i]=len(d)
            
        print(suffix)
        
        count=0
        for i in range(n):
            
            if prefix[i]==suffix[i]:
                count+=1
                
        return count