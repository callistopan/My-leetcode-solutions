class Solution {
public:
    long long matrixSumQueries(int n, vector<vector<int>>& queries) {
     vector<bool> rowFlag(n,1) , colFlag(n,1);
     long long ans = 0, rowRemain = n, colRemain = n;

     for (int i =queries.size()-1; i>=0 ; --i){
         if (queries[i][0]==0 && rowFlag[queries[i][1]]){
             ans += colRemain * queries[i][2];
             rowFlag[queries[i][1]] = 0;
             rowRemain--;
         }
          if (queries[i][0] == 1 && colFlag[queries[i][1]]){
             ans += rowRemain * queries[i][2];
             colFlag[queries[i][1]] = 0;
             colRemain--;
         }
     }
     return ans;
    }
};