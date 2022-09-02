class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n=grid.size();
        vector<int> row_max(n);
        vector<int> col_max(n);
        
        for (int r=0;r<n;r++){
            for (int c=0;c<n;c++){
                row_max[r]=max(row_max[r],grid[r][c]);
                col_max[c]=max(col_max[c],grid[r][c]);
            }
        }
        
        int ans=0;
         for (int r=0;r<n;r++){
            for (int c=0;c<n;c++){
                ans+=min(row_max[r],col_max[c])-grid[r][c];
            }
        }
        return ans;
        
    }
};