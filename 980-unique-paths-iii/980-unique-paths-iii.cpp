class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        
        auto i1=0, j1=0, t_steps=0;
        
        for (int i=0;i<grid.size();i++){
            for (int j=0;j<grid[0].size();j++){
                if (grid[i][j]==1){
                    i1=i;
                    j1=j;
                }
                if (grid[i][j]!=-1) ++t_steps;
            }
        }
        
        return dfs(grid,i1,j1,1,t_steps);
    }
    
    int dfs(vector<vector<int>>&grid,int i, int j , int s, int t_s){
        if (i<0 or j<0 or i>=grid.size() or j>= grid[0].size() or grid[i][j]==-1) return 0;
        if (grid[i][j]==2) return s==t_s ?1:0;
        grid[i][j]=-1;
        int paths=dfs(grid,i+1,j,s+1,t_s)+dfs(grid,i-1,j,s+1,t_s)+dfs(grid,i,j+1,s+1,t_s)+dfs(grid,i,j-1,s+1,t_s);
        grid[i][j]=0;
        return paths;
    }
    
};