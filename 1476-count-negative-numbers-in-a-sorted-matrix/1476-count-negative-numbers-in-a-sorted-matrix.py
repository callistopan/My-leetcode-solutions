class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        
        i=0
        j=columns-1
        count=0
        
        while i<rows and j>=0:
            if grid[i][j]>=0:
                count+=(j+1)
                i+=1
            else:
                j-=1
        return rows*columns-count