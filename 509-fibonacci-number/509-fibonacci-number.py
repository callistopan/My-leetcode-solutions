class Solution:
    def fib(self, n: int) -> int:
        
        memo={}
        def recur_fib(n):
            if n in memo:
                return memo[n]
            
            if n<2:
                return n
            
            else:
                res=recur_fib(n-1)+recur_fib(n-2)
                
            memo[n]=res
            
            return res
        
        return recur_fib(n)
            