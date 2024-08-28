class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        #dfs
        r=len(grid2)
        c=len(grid2[0])
        count=0
        for i in range(r):
            for j in range(c):
                if grid2[i][j]==1 and grid1[i][j]==1:
                    flag=[0]
                    self.bfs(grid1,grid2,i,j,flag)
                    if flag[0]==0:
                        count+=1
        return count
    def bfs(self,grid1,grid2,i,j,flag):
        r=len(grid1)
        c=len(grid1[0])
        q=[]
        q.append([i,j])
        while q:
            p=q.pop(0)
            n,m=p[0],p[1]
            if grid1[n][m]==0:
                flag[0]=1
            if self.is_safe(r,c,n-1,m) and grid2[n-1][m]==1:
                q.append([n-1,m])
                grid2[n-1][m]=-1
            if self.is_safe(r,c,n+1,m) and grid2[n+1][m]==1:
                q.append([n+1,m])
                grid2[n+1][m]=-1
            if self.is_safe(r,c,n,m-1) and grid2[n][m-1]==1:
                q.append([n,m-1])
                grid2[n][m-1]=-1
            if self.is_safe(r,c,n,m+1) and grid2[n][m+1]==1:
                q.append([n,m+1])
                grid2[n][m+1]=-1
    
    
    
    
    
    def is_safe(self,r,c,i,j):
        if i>=0 and i<r and j>=0 and j<c:
            return True
        else:
            return False

    
            
        
                    
                    