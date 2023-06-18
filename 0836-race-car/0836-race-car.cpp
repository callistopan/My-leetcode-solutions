class Solution {
public:
    int racecar(int target) {
        vector<int> dp(target+1,-1);
        dp[0]=0;
        return race_car_help(target,dp);

    }

    int race_car_help(int i, vector<int>& dp){
        if (dp[i] >= 0){
            return dp[i];
        }

        dp[i] = INT_MAX;

        int m =1 , j = 1;

        for (; j < i; j = (1 << ++m)-1){ // for all break points
            for (int q = 0 , p = 0 ; p < j; p = (1<< ++q)-1){
                dp[i] = min(dp[i], m+1+q+1+race_car_help(i-(j-p),dp));
            }
        }

        dp[i] = min(dp[i], m+ (i==j ? 0 : 1 + race_car_help(j-i,dp)));
        return dp[i];
    }
};