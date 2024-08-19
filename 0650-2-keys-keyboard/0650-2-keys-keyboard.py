class Solution:
    def minSteps(self, n: int) -> int:
        
        ## ans is sum of all prime factors of n
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans