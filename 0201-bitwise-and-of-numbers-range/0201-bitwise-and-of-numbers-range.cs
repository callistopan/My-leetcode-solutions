public class Solution {
    public int RangeBitwiseAnd(int m, int n) {
        int shift = 0;
        
        // find the common prefix
        while ( m < n){
            m >>= 1;
            n >>= 1;
            shift++;
        }
        
        // shift m back to the left by the number of shifts we made
        return m << shift;
    }
}