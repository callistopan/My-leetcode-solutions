class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long res = 0;
        int maxa  = 0 , maxab =0;
        // maxa is current maximum number
        // maxab is current maximum a-b ie nums[i]- nums[j]

        for (int& a : nums){
            res = max(res , 1LL * maxab * a);  
            maxab = max(maxab , maxa -a);
            maxa = max(maxa , a);
        }

        return res;
    }
};