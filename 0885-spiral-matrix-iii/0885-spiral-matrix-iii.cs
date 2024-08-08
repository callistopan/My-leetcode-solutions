public class Solution {
    public int[][] SpiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int[][] directions = new int[][]{
            new int[] {0,1},
            new int[] {1,0},
            new int[] {0,-1},
            new int[] {-1,0}
        };
        
        List<int[]> result = new List<int[]>();
        result.Add(new int[] {rStart, cStart});
        
        int steps = 1;
        int d = 0;
        
        while ( result.Count < rows * cols){
            for (int i = 0; i < 2; i++){
                for (int j = 0; j < steps; j++){
                    rStart += directions[d][0];
                    cStart += directions[d][1];
                    if ( 0 <= rStart && rStart < rows && 0 <= cStart && cStart < cols){
                        result.Add(new int[] {rStart, cStart });
                    }
                }
                d = (d + 1) % 4;
            }
            steps ++;
        }
        return result.ToArray();
    }
}