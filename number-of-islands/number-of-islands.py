class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count
    def dfs(self,grid,row,col):
        if 0>row or row>=len(grid) or col<0 or col>=len(grid[0]):
            return
        if grid[row][col]!='1':
            return
        grid[row][col]='$'
        self.dfs(grid,row+1,col)
        self.dfs(grid,row-1,col)
        self.dfs(grid,row,col+1)
        self.dfs(grid,row,col-1)