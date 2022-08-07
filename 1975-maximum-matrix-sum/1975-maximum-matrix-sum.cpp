class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& a) {
        //So, if the number of negative signs is even, the answer is the sum of the absolute value of all elements. If it is odd, we will have to minus 2 times the number with smallest absolute value (for we have to change + sign to -) to get the answer:
        
        long long neg_count=0;
        long long ans =0;
        long long n = a.size();
        long long min_element = 1000000;
        
        for ( int i=0; i<n;i++){
            
            for ( int j=0;j<n;j++){
                
                ans+=abs(a[i][j]);
                
                if (a[i][j]<0){
                    neg_count+=1;
                }
                min_element= min_element <abs(a[i][j]) ? min_element: abs(a[i][j]);
            }
        }
        
        if (neg_count%2==0){  // as there are even negative elements
            
            return ans;
        }
        else{  // there is odd -ve elements ,so we need to remain a negative element
            // which needs to be the smallest possible in the matrix
            
            return ans- 2*min_element;
            
        }
        
        
    }
};