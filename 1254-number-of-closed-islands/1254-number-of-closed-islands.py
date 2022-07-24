class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # exclude connected zeros on corner 
        # push all 0's on the corner to queue
        
        r=len(grid)
        c=len(grid[0])
        
        q = deque()
        
        for i in range(r):
            
            if grid[i][0]==0:
                q.append((i,0))
                
            if grid[i][c-1]==0:
                q.append((i,c-1))
                
        for i in range(1,c-1):
            
            if grid[0][i]==0:
                q.append((0,i))
                
            if grid[r-1][i]==0:
                q.append((r-1,i))
                
        # make all 0's connected 1
        
        while q:
            
            i,j = q.popleft()
            grid[i][j]=1
            
            if i-1>=0 and grid[i-1][j]==0:
                q.append((i-1,j))
                
            if i+1<r and grid[i+1][j]==0:
                q.append((i+1,j))
                
            if j-1>=0 and grid[i][j-1]==0:
                q.append((i,j-1))
            if j+1<c and grid[i][j+1]==0:
                q.append((i,j+1))
                
        # count connected components 
        count=0
        for i in range(r):
            for j in range(c):
                
                if grid[i][j]==0:
                    self.dfs(grid,i,j)
                    count+=1
                    
        return count
    
    
    def dfs(self,grid,i,j):
        
        if i<0 or i>=len(grid) or j<0 or j>= len(grid[0]):
            return
        
        if grid[i][j]!=0:
            return
        
        grid[i][j]=1
        
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    