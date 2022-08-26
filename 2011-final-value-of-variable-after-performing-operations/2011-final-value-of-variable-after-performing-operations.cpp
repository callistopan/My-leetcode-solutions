class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        
        int x=0;
        for (auto v :operations){
            if (v=="++X" or v=="X++"){
                x++;
            }
            else{
                x--;
            }
        }
        return x;
        
    }
};