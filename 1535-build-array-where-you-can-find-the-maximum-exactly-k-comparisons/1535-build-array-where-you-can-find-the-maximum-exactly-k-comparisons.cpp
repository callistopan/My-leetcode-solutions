class Solution {
    // time complexity : O(n.m^2.k) as nmk possible states for dp and we use for loop (m)
    // space : O(n.m.k) for dp
public:
    vector<vector<vector<int>>> memo;
    int MOD = 1e9 +7;
    int n, m;

    int numOfArrays(int n, int m, int k) {
        memo = vector(n, vector(m+1,vector(k+1,-1)));
        this->n = n;
        this->m = m;
        return dp(0,0,k);


    }

    int dp(int i , int maxSoFar , int remain){
        if ( i==n){// length of array
            if (remain ==0){ // remaining cost is zero
                return 1;
            }
            return 0;
        }

        if (remain < 0){
            return 0;
        }

        if( memo[i][maxSoFar][remain] != -1){
            return memo[i][maxSoFar][remain];
        }

        int ans = 0;
        for (int num = 1 ; num <= maxSoFar ; num++){
            ans = (ans + dp(i+1 , maxSoFar , remain)) % MOD; //we place not a new maximum here
        }

        for( int num = maxSoFar +1 ; num <=m; num++){
            ans = (ans + dp(i+1, num , remain -1)) % MOD; // we place a newer maximum here ie maxSoFar + 1 , maxSoFar+2....... m
        }
        memo[i][maxSoFar][remain] = ans;
        return ans;
    }
};