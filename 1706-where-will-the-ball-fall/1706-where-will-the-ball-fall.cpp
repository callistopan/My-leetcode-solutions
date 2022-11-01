class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int n =grid[0].size();
        vector<int> ans;
        for (int i=0;i<n;i++){
            ans.push_back(dfs(grid,0,i));
        }
        return ans;
    }
    int dfs(vector<vector<int>>& grid,int r,int c){
        if (r==grid.size())
            return c;
        else if (grid[r][c]==1 and (c+1<grid[0].size()) and grid[r][c+1]==1)
            return dfs(grid,r+1,c+1);
        else if (grid[r][c]==-1 and 0<=c-1 and grid[r][c-1]==-1)
            return dfs(grid,r+1,c-1);
        else
            return -1;
    }
};


