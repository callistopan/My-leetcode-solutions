public class Solution {
    public int MaxTurbulenceSize(int[] arr) {
        if (arr.Length == 1){
            return 1;
        }
        int up = 1, down =1;
        int maxLen = 1;
        for (int i = 1; i < arr.Length; i++){
            if (arr[i] > arr[i-1]){ // found up
                up = down + 1;
                down = 1;
            }
            else if ( arr[i] < arr[i-1]){
                down = up + 1;
                up = 1;
            }
            else{
                down = 1;
                up = 1;
            }
            maxLen = Math.Max(maxLen,Math.Max(up,down));
        }
        return maxLen;
    }
}