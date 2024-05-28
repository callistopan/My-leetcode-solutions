class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n = len(s)
        res = 0
        l = 0
        curr = 0
        for r in range(n):
            
            curr += abs(ord(s[r]) - ord(t[r]))
                        
            while curr > maxCost and l < n:
                curr -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            res = max(res, r - l + 1)
            r+=1
        return res