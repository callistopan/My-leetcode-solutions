class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        long long n = grid[0].size();
        vector<long long> prefix_sum_upper(n);
        vector<long long> prefix_sum_lower(n);

        prefix_sum_upper[0] = grid[0][0];
        prefix_sum_lower[0] = grid[1][0];
        for (long long i = 1; i < n ;i++){
            prefix_sum_upper[i] = prefix_sum_upper[i-1] + grid[0][i];
            prefix_sum_lower[i] = prefix_sum_lower[i-1] + grid[1][i];

        }
      
        long long score_2 = 1234567890123456789LL;
        for (long long i = 0; i < n;i++){
            score_2 = min(score_2, max(prefix_sum_upper[n-1]-prefix_sum_upper[i],prefix_sum_lower[i]- grid[1][i]));
        }

        return score_2;
       


    }
};