class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        ''' if the cell is pard of pyramid then just increase it's value
            do this for reversed matrix also'''
        reversed_grid= []
        
        for i in range(len(grid)-1,-1,-1):
            reversed_grid.append(grid[i][:])
            
        res = self.helper(grid)
        res+=self.helper(reversed_grid)
        
        return res
    
    
    def helper(self,grid):
        
        res =0
        r =len(grid)
        c =len(grid[0])
        
        for i in range(1,r):
            for j in range(1,c-1):
                
                if grid[i][j] and grid[i-1][j]:
                    
                    grid[i][j]=min(grid[i-1][j-1],grid[i-1][j+1]) +1
                    
                    res += grid[i][j]-1
                    
        return res
                