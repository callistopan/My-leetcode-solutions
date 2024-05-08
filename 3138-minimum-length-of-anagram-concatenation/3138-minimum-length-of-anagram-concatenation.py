class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for i in range(1,n//2 +1):
            if n % i == 0 and self.ok(s, i):
                return i
        return n
    def ok(self,s,k):
        n = len(s)
        cnt1 = Counter(s[:k])
        
        for i in range(k,n,k):
            cnt2 = Counter(s[i: i +k])
            if cnt1 != cnt2:
                return False
        return True