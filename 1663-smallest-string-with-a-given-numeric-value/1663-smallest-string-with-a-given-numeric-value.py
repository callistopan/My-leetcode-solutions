class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        # put highest possible character at the end
        # to check possible if we put the charcter then if remaining of k is less than remaining of  characters to put then we need to decrease the char from z to y up to a
        
        
        s =''
        
        for i in range(n):
            
            for j in range(ord('z')-ord('a'),-1,-1):
                
                if k-j+1 >= n-i+1:
                    
                    s+=chr(j+ord('a'))
                    
                    k= k-j-1
                    
                    break
                    
        return s[::-1]