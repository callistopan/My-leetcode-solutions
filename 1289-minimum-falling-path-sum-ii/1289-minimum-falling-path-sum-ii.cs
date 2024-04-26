public class Solution {
    private int[,] dp;
    
    public int MinFallingPathSum(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        dp = new int[n, m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dp[i, j] = -1;
            }
        }
        
        int res = int.MaxValue;
        
        for (int j = 0; j < m; j++) {
            res = Math.Min(res, grid[0][j] + DFS(grid, 1, j));
        }
        
        return res;  
    }
    
    private int DFS(int[][] arr, int row, int prevCol) {
        if (row == arr.Length) {
            return 0;
        }
        
        if (dp[row, prevCol] != -1) {
            return dp[row, prevCol];
        }
        
        int minSum = int.MaxValue;
        
        for (int j = 0; j < arr[0].Length; j++) {
            if (j != prevCol) {
                minSum = Math.Min(minSum, arr[row][j] + DFS(arr, row + 1, j));
            }
            
        }
        
        
        dp[row, prevCol] = minSum;
        return minSum;
    }
}
