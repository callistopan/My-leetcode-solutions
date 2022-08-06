class Solution:
    def numPermsDISequence(self, s: str) -> int:
        
        n= len(s)
        
        mod= 10**9+7
        
        #dp[i][j]
        # i means the the first i digits
        # j means the rest of the unused digits
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        
        for j in range(n+1):
            dp[0][j]=1
            
        for i in range(n):
            
            if s[i]=='I':
                
                curr=0
                for j in range(0,n-i):
                    dp[i+1][j]= curr =(curr+dp[i][j])%mod
                    
            else:
                
                curr=0
                for j in range(n-i-1,-1,-1):
                    dp[i+1][j]= curr =(curr+dp[i][j+1]) % mod
                    
        return dp[n][0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l= [i for i in range(len(s)+1)]
#         p=list(itertools.permutations(l))
        
#         # check if the the permutation is valid
#         c=0
#         for i in p:
            
#             j=0
#             flag=1
            
#             for k in range(1,len(i)):
                
#                 if i[k]<i[k-1] and s[j]=='I':
#                     flag=0
                    
#                     break
#                 elif i[k]> i[k-1] and s[j]=='D':
#                     flag=0
#                     break
#                 j+=1
                    
#             if flag:
#                 c+=1
                
#         return c
                
        