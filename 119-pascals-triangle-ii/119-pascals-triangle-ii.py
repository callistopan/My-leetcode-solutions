class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        '''  using O(n) space'''
        
        pascal = [1]*(rowIndex + 1)
        
        print(pascal)
        
        for i in range(2,rowIndex+1):
            
            for j in range(i-1,0,-1): # not including the last index and first index
                
                pascal[j] += pascal[j-1]  
                
            print(pascal)
                
        return pascal