public class Solution {
    public int NumMusicPlaylists(int n, int goal, int k) {
        
        const int Mod = 1000000007;

        // dp table 

        long[,] dp= new long[goal+1,n+1];

        for (int i = 0 ; i <= goal;i++){
            for (int j = 0 ; j<=n;j++){
                dp[i,j]=0;
            }
        }

        dp[0,0] = 1;

        for (int i = 1; i<=goal ; i++){
            for(int j = 1; j<=Math.Min(i,n); j++){

                // ith song is a new song

                dp[i,j] = (dp[i-1,j-1] * (n-j+1)) % Mod;  // one less new song * number of remaining unique songs

                // i th song is already played before

                if (j >k){
                    dp[i,j] = (dp[i,j] + dp[i-1,j]*(j-k)) %Mod; // one less song and number of songs we can play before k from current
                }
            }
        }
        return (int)dp[goal,n];
    }
}