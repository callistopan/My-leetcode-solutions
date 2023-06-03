class Solution {
public:
    vector<vector<int>> differenceOfDistinctValues(vector<vector<int>>& grid) {
        int m = grid.size(), n= grid[0].size();
        vector<vector<int>> res(m,vector<int>(n));
        auto populateDiag = [&](int i ,int j){
            unordered_set<int> top_left , bottom_right;
            // forward traversal
            for (int d =0; i+d <m && j+d <n;++d){
                res[i+d][j+d] = top_left.size();
                top_left.insert(grid[i+d][j+d]);
            }
            // reverse traversal
            for (int d = min(m-i,n-j)-1; d>=0; --d){
                res[i+d][j+d] = abs(res[i+d][j+d] - (int)bottom_right.size());
                bottom_right.insert(grid[i+d][j+d]);
                
            }
        };
        for (int j = 0; j < n; ++j)
            populateDiag(0, j);
        for (int i = 1; i < m; ++i)
            populateDiag(i, 0);
        return res;


    }
};