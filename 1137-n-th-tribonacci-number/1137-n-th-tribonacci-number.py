class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n<=2:
            return 1
        
        f=[0]*(n+1)
        f[0]=0
        f[1]=1
        f[2]=1
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]+f[i-3]
        return f[n]
  