class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        int res=0;
        vector<vector<int>> dp( r , vector<int> (c, 0));
       
        for (int j = 1;j < c;j++){
            for (int i = 0;i < r;i++){
                dp[i][j]= max(i-1>=0 && grid[i-1][j-1] < grid[i][j]? dp[i-1][j-1]+1: 0,i+1<r && grid[i+1][j-1] < grid[i][j] ? dp[i+1][j-1]+1 : 0);
                dp[i][j]=max(dp[i][j],grid[i][j-1] < grid[i][j] ? dp[i][j-1]+1:0);
                
                if (dp[i][j]==0){
                    grid[i][j]=1000000;
                }
                res = max(res,dp[i][j]);
            }
        }
        return res;
        
        
    }
};