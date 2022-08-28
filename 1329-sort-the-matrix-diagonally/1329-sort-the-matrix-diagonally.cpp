class Solution {
public:
    /*
          time complexity  =O(MNLogD) D is the length of the diagonal of matrix
          space complexity=O(MN)
    */
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m=mat.size(),n=mat[0].size();
        unordered_map<int,priority_queue<int,vector<int>,greater<int>>>d; // min heap
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                d[i-j].push(mat[i][j]);
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                mat[i][j]=d[i-j].top();
                d[i-j].pop();
            }
        }
        return mat;
        
    }
};

