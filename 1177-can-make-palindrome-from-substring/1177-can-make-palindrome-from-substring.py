class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        
        dp = [collections.Counter()]
        for i in range(1, len(s)+1):
            dp.append(dp[i-1] + collections.Counter(s[i-1]))
        ans = []
        for l, r, k in queries:
                
            c = dp[r+1] - dp[l]
            need = sum(v % 2 for v in c.values()) // 2
            ans.append(need <= k)
        return ans