public class Solution {
    public bool CanArrange(int[] arr, int k) {
        Dictionary<int,int> remainderCount = new Dictionary<int,int>();
        
        foreach (int i in arr){
            int remainder = (i % k + k) % k;
            if (remainderCount.ContainsKey(remainder)){
                remainderCount[remainder] += 1;
            }
            else{
                remainderCount[remainder] = 1;
            }
        }
        
        foreach (int i in arr){
            int remainder = ( i % k + k) % k;
            
            if ( remainder == 0){
                if (remainderCount[0] % 2 == 1){
                    return false;
                }
            }
            else if (!remainderCount.ContainsKey(k - remainder) || remainderCount[remainder] != remainderCount[k - remainder]){
                return false;
            }
        }
        return true;
    }
}