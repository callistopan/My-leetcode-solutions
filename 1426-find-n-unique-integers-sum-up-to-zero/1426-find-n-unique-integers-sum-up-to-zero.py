class Solution:
    def sumZero(self, n: int) -> List[int]:
        res =[]
        first = -(n//2)
        if n&1:
          
            while n:
                res.append(first)
                first+=1
                n -=1
        

        else:
            
            while n:
                res.append(first)
                if first==-1:
                    first+=2
                else:
                    first+=1
                n-=1
        return res
            