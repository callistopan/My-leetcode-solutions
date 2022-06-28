class Solution:
    def divide(self, A: int, B: int) -> int:
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        power=32
        b_power=b<<power
        while a>=b:
            while b_power >a:
                b_power>>=1
                power-=1
            res+=1<<power
            a-=b_power
        
                
        return res if (A > 0) == (B > 0) else -res
