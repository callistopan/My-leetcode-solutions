class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n :
            return -1
        res = 0
        
        for i in range(30):
            if (n >> i & 1) != (k >> i & 1): # If bits are different , 10 or 01
                if n >> i & 1: # it should be 10 , 01 means no answer
                    res +=1
                else:
                    return -1
        return res