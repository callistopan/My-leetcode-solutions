class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            if s[i] =='[':
                count += 1
            else:
                if count:
                    count -=1
        return (count + 1)//2
        