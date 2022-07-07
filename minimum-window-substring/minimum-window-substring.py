class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ''' O (m+n)'''
        if not s or not t:
            return ""
        dict_t=Counter(t)
        required=len(dict_t)  #required characters
        
        l=0
        r=0
        
        formed=0
        window_counts={}
        ans=float("inf"),None,None    #window length ,left,right
        
        ''' O(2* len(s))'''
        while r<len(s):
            window_counts[s[r]]=window_counts.get(s[r],0)+1
            
            if s[r] in dict_t and window_counts[s[r]]==dict_t[s[r]]:  # successfully formed one character
                formed+=1
                
            
            while l<=r and formed==required:  # we have all the required characters
                
                if r-l+1<ans[0]:
                    ans=((r-l+1),l,r)
                    
                #remove left
                window_counts[s[l]]-=1
                if s[l] in dict_t and window_counts[s[l]]<dict_t[s[l]]:  # if we are removing the character which is in t
                    formed-=1
                    
                l+=1
                
            r+=1
            
        return '' if ans[0]==float("inf") else s[ans[1]:ans[2]+1]