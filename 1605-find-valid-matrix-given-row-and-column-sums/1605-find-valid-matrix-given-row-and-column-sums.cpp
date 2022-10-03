class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        // find smallest rowsum or columnsum each time and place it there
        int n=rowSum.size();
        int m=colSum.size();
        vector<vector<int>> mat(n,vector<int> (m,0));
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                int x=min(rowSum[i],colSum[j]);
                mat[i][j]=x;
                rowSum[i]-=x;
                colSum[j]-=x;
        
            }
        }
        return mat;
        
    }
};