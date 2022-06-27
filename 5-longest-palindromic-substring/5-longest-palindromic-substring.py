class Solution:
    def longestPalindrome(self, s: str) -> str:
        left=0
        right=0
        m=1
        n=len(s)
        for i in range(1,n):
            l=i
            r=i
            
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if s[l]==s[r] and r-l+1 >=m:
                m=r-l+1
                left=l
                right=r
            l=i-1
            r=i
            
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if s[l]==s[r] and r-l+1 >=m:
                m=r-l+1
                left=l
                right=r
        return s[left:right+1]