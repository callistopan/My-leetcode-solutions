class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        half = (n + 1)//2 # example , n = 5 , half = 3
        res = 0
        seen = set()
        
        for v in range( 10**(half - 1), 10**(half)): # 100 -> 1000 ( 100 to 999)
            vv = str(v) + str(v)[::-1][n % 2:] # 233 + 32 = "23332", 109+ 01 = "10901"
            key = ''.join(sorted(vv))
            
            if int(vv) % k == 0 and key not in seen:
                seen.add(key)
                count = Counter(vv) # for finding the duplicates for "10901" {1:2, 0:2, 9:1}
                x = (n - count['0']) * factorial(n - 1)
                '''
                   10901 => first position cannot be 0 so (5 - 2)
                   Already placed one number on first position, so we can take remaining 4
                   so (5 - 2)*4*3*2*1 total permutations
                
                '''
                
                for i,c in count.items():
                    # Remove duplicates to handle repeated digits
                    x //= factorial(c)
                
                res += x
        return res
            