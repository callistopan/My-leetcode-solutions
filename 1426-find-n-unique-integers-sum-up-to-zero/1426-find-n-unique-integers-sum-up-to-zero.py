class Solution:
    def sumZero(self, n: int) -> List[int]:
        res =[]
        first = -(n//2) 
        k = n   
        while n:
            res.append(first)
            if first==-1 and k&1==0:
                first+=2
            else:
                first+=1
            n-=1
        return res
            