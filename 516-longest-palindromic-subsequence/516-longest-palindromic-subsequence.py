'''If the two ends of a string are the same, then they must be included in the longest palindrome subsequence. Otherwise, both ends cannot be included in the longest palindrome subsequence.'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        return self.longest(0,len(s)-1,s)
    
    @lru_cache(None)
    def longest(self,l,r,s):
        
        if l==r:
            return 1
        if l>r:
            return 0
        
        return 2+self.longest(l+1,r-1,s) if s[l]==s[r] else max(self.longest(l+1,r,s),self.longest(l,r-1,s))
    
    