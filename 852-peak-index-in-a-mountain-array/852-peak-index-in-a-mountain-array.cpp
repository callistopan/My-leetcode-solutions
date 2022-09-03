class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // 1,2,3,5,4,2,0
        // if left element exists and it is less than middle then we need to consider right side of array
        // our condition is left <middle<right
        int n=arr.size();
        int l=0;
        int r=n-1;
        
        while (l<=r){
            int m=l+(r-l)/2;
            
            if (m==0){
                l=m+1;
            }
            else if (m==n-1){
                r=m-1;
                
            }
            else if (arr[m-1]<arr[m] and arr[m]>arr[m+1]){
                return m;
            }
            else if (arr[m-1]<arr[m]){
                l=m+1;
            }
            else{
                r=m-1;
            }
        }
        return -1;
        
        
    }
};