class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo={}
        
        def recurse(i,curr_char,run_len,k):
            
            if i==len(s):
                return 0
            
            if (i,curr_char,run_len,k) in memo:
                return memo[(i,curr_char,run_len,k)]
            
            #delete
            delete_cost= float('inf')
            if k>0:
                delete_cost=recurse(i+1,curr_char,run_len,k-1)
                
            keep_score=0
            
            if s[i]==curr_char:
                
                extra_cost=0
                if run_len==1 or len(str(run_len+1))>len(str(run_len)):
                    extra_cost=1
                    
                keep_cost=extra_cost+recurse(i+1,curr_char,run_len+1,k)
                
            else:
                keep_cost=1+recurse(i+1,s[i],1,k)
                
            memo[(i,curr_char,run_len,k)]=min(delete_cost,keep_cost)
            
            return memo[(i,curr_char,run_len,k)]
        return recurse(0,'',0,k)