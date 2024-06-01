class Solution:
    def numDecodings(self, s: str) -> int:
        self.mod = 1000000007
        self.memo = {}
        n = len(s)
        return self.dfs(s, n - 1)
    
    def dfs(self,s,i):
        if i < 0:
            return 1
        if i in self.memo:
            return self.memo[i]
        
        if s[i] == "*":
            res = 9 * self.dfs(s, i - 1) % self.mod
            
            if i and s[i-1] == "1":
                res = ( res + 9 * self.dfs(s, i - 2)) % self.mod
            
            elif i and s[i-1] =="2":
                res = ( res + 6 * self.dfs(s, i - 2)) % self.mod
            
            elif i and s[i-1] == "*":
                res = ( res + 15 * self.dfs(s, i - 2)) % self.mod
            
            self.memo[i] = res
            return res
        
        res = self.dfs(s, i - 1) if s[i] != "0" else 0
        
        if i and s[i-1] == "1":
            res = ( res + self.dfs(s, i - 2)) % self.mod
        
        elif i and s[i-1] == "2" and s[i] <= "6":
            res = ( res + self.dfs(s, i - 2)) % self.mod
        
        elif i and s[i-1] == "*":
            res = ( res + (2 if s[i] <= "6" else 1) * self.dfs(s, i - 2))% self.mod
        
        self.memo[i] = res
        return res
            
            
            
            
            
            
            
            
            
            
            
        