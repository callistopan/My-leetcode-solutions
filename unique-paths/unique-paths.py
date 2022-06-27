class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=m+n-2
        t=comb(x,n-1)
        return t