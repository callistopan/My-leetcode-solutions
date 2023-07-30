class Solution {
public:
    int strangePrinter(string s) {
        int n = s.size();
        vector dp(n,vector<int>(n,n)); //  initialise with a larger value as we want minimised result 

        for (int length = 1; length <= n ; length++){  // for all possible length of substrings
            for (int left = 0; left <= n - length ; left++){ // starting position of substring or left
                int right = left + length -1;  // length = right -left +1 so right = left + length -1
                int j = -1;   
                for (int i = left ; i<right;i++){
                    if (s[i]!= s[right] && j==-1){  // first inequality of characters
                        j = i;
                    }
                    if (j !=-1){
                        dp[left][right] = min(dp[left][right], 1+ dp[j][i] + dp[i+1][right]); // 1 for changing the current character  dp[j][i] for changing the previos ones and dp[i+1][right] for changing the rest of the characters , these all already calculated with smaller lengths so we know their values already
                    }
                }

                if (j==-1){ // all characters are same
                    dp[left][right] = 0;
                }
            }
        }
        return dp[0][n-1] + 1; // +1 for initial operation (set all characters the same - the last character)
        
    }
};